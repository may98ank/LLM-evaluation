import os, json, shutil, subprocess, time, random, requests
from openai import OpenAI

# === CONFIG ===
BASE_SOURCE = "exercise2_data_singlek"
TARGET_BASE = "exercise2_part2"
ITERATIONS = 3
MODEL = "gpt-4o-mini"  # try gpt-3.5-turbo if needed
SELECTED = [
    ("HumanEval_125", "DeepSeek_Checklist_k0"),
    ("HumanEval_24", "DeepSeek_CoT_k0")
]

# === RATE / THROTTLE SETTINGS ===
MAX_TOKENS_PER_CALL = 20000
SECONDS_BETWEEN_CALLS = 70   # 1 call per minute
BACKOFF_BASE = 60             # retry delay base for 429s

# === INITIALIZE ===
client = OpenAI(api_key="")

# --- Helpers ---
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def copy_baseline(task, combo):
    src_path = os.path.join(BASE_SOURCE, task, combo)
    dest_path = os.path.join(TARGET_BASE, task, combo, "iteration_0")
    ensure_dir(dest_path)
    shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
    return dest_path

def run_coverage(iter_dir):
    env = os.environ.copy()
    env["PYTHONPATH"] = "./"
    cmd = ["pytest", "--cov=src", "--cov-branch", "--cov-report=term", "-q"]
    result = subprocess.run(cmd, cwd=iter_dir, capture_output=True, text=True, env=env)
    return result.stdout + result.stderr

def extract_cov(text):
    """Parse pytest output for line & branch coverage."""
    line_cov, branch_cov = None, None
    for line in text.splitlines():
        if "TOTAL" in line:
            parts = line.split()
            try:
                line_cov = float(parts[-1].replace("%", ""))
            except Exception:
                pass
    return line_cov, branch_cov

# === Local Ollama fallback ===
def ollama_generate(prompt, model="qwen2.5-coder:3b"):
    body = {"model": model, "prompt": prompt, "stream": False, "options": {"temperature": 0.3}}
    try:
        r = requests.post("http://localhost:11434/api/generate", json=body, timeout=120)
        return r.json().get("response", "")
    except Exception as e:
        print(f"⚠️ Ollama fallback failed: {e}")
        return ""

# === Throttled OpenAI generation ===
def safe_generate(prompt):
    """Auto-throttle & retry if rate limit or network errors occur."""
    for attempt in range(4):
        try:
            resp = client.responses.create(model=MODEL, input=prompt, temperature=0.3)
            text = resp.output_text.strip()
            print(f"✅ LLM response received ({len(text)} chars).")
            time.sleep(SECONDS_BETWEEN_CALLS)  # pacing
            return text
        except Exception as e:
            if "Rate limit" in str(e) or "429" in str(e):
                wait = BACKOFF_BASE * (2 ** attempt) + random.randint(0, 30)
                print(f"⏳ Rate limit reached — waiting {wait}s before retry...")
                time.sleep(wait)
            else:
                print(f"⚠️ OpenAI error ({e}) — falling back to Ollama.")
                return ollama_generate(prompt)
    print("❌ Exhausted retries — skipping iteration.")
    return ""

# === Main routine ===
def improve_tests(task, combo):
    print(f"\n=== Running LLM-assisted iterations for {task}/{combo} ===")
    combo_path = os.path.join(TARGET_BASE, task, combo)
    ensure_dir(combo_path)
    coverage_history = []

    # baseline copy
    baseline = copy_baseline(task, combo)
    coverage = run_coverage(baseline)
    lcov, bcov = extract_cov(coverage)
    coverage_history.append({"iteration": 0, "line": lcov, "branch": bcov})
    print(f"Baseline: line={lcov}, branch={bcov}")

    for i in range(1, ITERATIONS + 1):
        prev_iter = os.path.join(combo_path, f"iteration_{i-1}")
        next_iter = os.path.join(combo_path, f"iteration_{i}")
        ensure_dir(next_iter)
        ensure_dir(os.path.join(next_iter, "tests"))
        ensure_dir(os.path.join(next_iter, "src"))

        # Copy solution forward
        shutil.copytree(os.path.join(prev_iter, "src"), os.path.join(next_iter, "src"), dirs_exist_ok=True)

        # Read code & partial tests
        code_file = os.path.join(prev_iter, "src/solution.py")
        test_file = os.path.join(prev_iter, "tests/test_solution.py")
        with open(code_file) as f: code = f.read()
        with open(test_file) as f: old_tests = f.read()

        # Reduce prompt size
        tail_tests = "\n".join(old_tests.splitlines()[-40:])

        prompt = f"""
You are improving a pytest suite to increase branch coverage.
Below is the Python function followed by the *last 40 lines* of current tests.

### Function
{code}

### Existing tests
{tail_tests}

Add 3-5 new pytest test functions that explore:
- Edge conditions
- Alternate branches (if/else, exceptions)
Avoid duplicates. Name them test_case_<n>.
Return only Python test code, no explanations.
"""

        print(f"Iteration {i}: generating improved tests...")
        new_tests = safe_generate(prompt)

        # Merge and save
        merged = old_tests + "\n\n# === LLM iteration {} ===\n".format(i) + new_tests
        out_test = os.path.join(next_iter, "tests/test_solution.py")
        with open(out_test, "w") as f: f.write(merged)

        # Run coverage
        print(f"Iteration {i}: running coverage...")
        cov_out = run_coverage(next_iter)
        lcov, bcov = extract_cov(cov_out)
        coverage_history.append({"iteration": i, "line": lcov, "branch": bcov})
        print(f"Iteration {i}: line={lcov}, branch={bcov}")

        # Convergence check
        if i >= 2:
            prev2 = coverage_history[-3]["line"] or 0
            curr = coverage_history[-1]["line"] or 0
            if abs(curr - prev2) <= 3:
                print(f"✅ Converged after {i} iterations (<3%)")
                break

    cov_path = os.path.join(combo_path, "coverage.json")
    with open(cov_path, "w") as f:
        json.dump(coverage_history, f, indent=2)
    print(f"✅ Saved → {cov_path}")

# === Run selected tasks ===
for task, combo in SELECTED:
    improve_tests(task, combo)
