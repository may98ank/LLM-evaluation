# Exercise 2
**COMPSCI 520 — Theory and Practice of Software Engineering**  
**Author:** Fnu Mayank  

## Part 1 — Baseline Coverage Analysis

### Objective
The goal of this part is to establish a **baseline for test coverage** across all HumanEval problems and model-generated solutions (DeepSeek vs Qwen; Checklist vs CoT strategies).  
We automated coverage collection to measure **line coverage**, **branch coverage**, and **number of tests passed** for each problem.  
The results serve as a reference for evaluating future improvements in code correctness and test quality.

---

### Methodology
1. **Dataset Preparation (Exercise 1 Outputs):**  
   Each HumanEval task’s model-generated code (`k0`) was paired with its respective benchmark test file.  
   Directory structure was standardized as:
```HumanEval_<ID>/<Model>/<Strategy>/k0.py```
javascript
Copy code
Each directory included a corresponding `tests/test_solution.py` file importing and executing the model’s function.

2. **Coverage Measurement:**  
We used `pytest` with the `pytest-cov` plugin to collect line and branch coverage:  
```
PYTHONPATH=./ pytest --cov=src --cov-branch
```
This recorded executed lines and branches while running unit tests.

Each entry represents one `(task, model, prompting-strategy)` combination evaluated with the HumanEval test suite.

---

### Coverage Summary

| Task | Combo | Tests Total | Tests Passed | Line Coverage (%) | Branch Coverage (%) | Notes |
|------|--------|-------------|---------------|-------------------|--------------------|-------|
| HumanEval_101 | Qwen_CoT_k0 | 0 | 0 |  –  |  –  | No tests discovered. |
| HumanEval_101 | Qwen_Checklist_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_101 | DeepSeek_CoT_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_101 | DeepSeek_Checklist_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_66 | Qwen_CoT_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_66 | Qwen_Checklist_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_66 | DeepSeek_CoT_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_66 | DeepSeek_Checklist_k0 | 0 | 0 |  –  |  –  | No tests discovered. |
| HumanEval_50 | Qwen_CoT_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_50 | Qwen_Checklist_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_50 | DeepSeek_CoT_k0 | 0 | 0 |  –  |  –  | No tests discovered. |
| HumanEval_50 | DeepSeek_Checklist_k0 | 0 | 0 |  –  |  –  | No tests discovered. |
| HumanEval_51 | Qwen_CoT_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_51 | Qwen_Checklist_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_51 | DeepSeek_CoT_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_51 | DeepSeek_Checklist_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_125 | Qwen_CoT_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_125 | Qwen_Checklist_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_125 | DeepSeek_CoT_k0 | 0 | 0 |  –  |  –  | No tests discovered. |
| HumanEval_125 | DeepSeek_Checklist_k0 | 1 | 0 | 45.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_147 | Qwen_CoT_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_147 | Qwen_Checklist_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_147 | DeepSeek_CoT_k0 | 0 | 0 |  –  |  –  | No tests discovered. |
| HumanEval_147 | DeepSeek_Checklist_k0 | 1 | 0 | 50.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_134 | Qwen_CoT_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_134 | Qwen_Checklist_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_134 | DeepSeek_CoT_k0 | 0 | 0 |  –  |  –  | No tests discovered. |
| HumanEval_134 | DeepSeek_Checklist_k0 | 0 | 0 |  –  |  –  | No tests discovered. |
| HumanEval_24 | Qwen_CoT_k0 | 1 | 1 | 92.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_24 | Qwen_Checklist_k0 | 1 | 1 | 91.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_24 | DeepSeek_CoT_k0 | 1 | 0 | 50.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_24 | DeepSeek_Checklist_k0 | 1 | 0 | 67.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_52 | Qwen_CoT_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_52 | Qwen_Checklist_k0 | 1 | 1 | 100.0 |  –  | Low branch coverage — missing else/edge conditions. |
| HumanEval_52 | DeepSeek_CoT_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_52 | DeepSeek_Checklist_k0 | 0 | 0 |  –  |  –  | No tests discovered. |
| HumanEval_145 | Qwen_CoT_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_145 | Qwen_Checklist_k0 | 1 | 0 | 100.0 |  –  | Tests failed — logic error despite coverage. |
| HumanEval_145 | DeepSeek_CoT_k0 | 0 | 0 |  –  |  –  | No tests discovered. |
| HumanEval_145 | DeepSeek_Checklist_k0 | 0 | 0 |  –  |  –  | No tests discovered. |

---

### Interpretation

- **High coverage but failed tests** (e.g., *HumanEval_101*, *HumanEval_24*, *HumanEval_51*):  
  The generated function executes all lines but produces incorrect logic.  
  This suggests the model implemented wrong condition handling or return values.

- **Low branch coverage** (e.g., *Qwen_CoT_k0*, *Qwen_Checklist_k0*):  
  The tests exercise main paths but not alternate `if/else` or boundary conditions.  
  This is expected since HumanEval unit tests are concise and LLMs tend to generate straightforward, non-defensive logic.

- **No tests discovered**:  
  Usually indicates mismatched function names or import errors (e.g., test expected `solution()` while model defined a custom name).

- **45–67 % coverage**:  
  Implies partial execution — likely missing early-return or error-handling branches.

---

### Conclusion

The baseline coverage analysis shows that:
1. **Logic correctness** remains the dominant failure point even under full execution coverage.  
2. **Branch coverage** highlights missing test diversity better than line coverage.  
3. Many failures stem from **naming mismatches** or **unreached code paths**, not lack of code execution.  


---

## Part 2 - LLM-Assisted Test Generation & Coverage Improvement
### Step 1 — Selecting Problems
We are choosing tasks with the largest difference between test success % and branch coverage %.

|Task|Generated|Cov|Branch|Cov|TestsPassed|
|----|---------|---|------|---|-----------|
|HumanEval_125|DeepSeek_Checklist_k0|45%|–|0/1|	
|HumanEval_24|DeepSeek_CoT_k0|50%|–|0/1|	

These two have:

Moderate line coverage but failing tests → indicating logic bugs and untested branches.

Clear room for improvement with LLM-generated tests.

We’ll choose:
* HumanEval_125 – DeepSeek_Checklist_k0
* HumanEval_24 – DeepSeek_CoT_k0

### Step 2 — Prompts for LLM to produce new or improved tests.
The key is to direct the LLM toward branch-focused test creation, not just random input generation.

### Prompt template:
“You are improving a unit-test suite.
Below is the function implementation and existing tests.
Generate additional pytest-style tests that increase branch coverage.
Focus on edge conditions, alternate paths, and exception handling.
Avoid duplicates and trivial variations.
Return only valid Python code with test functions named test_case_<n>.”

The OpenAI gpt-4o-mini model was used with temperature = 0.3.

### Iterative Coverage Results

| Task / Combo | Iteration | New Tests Added | Line Coverage (%) | Branch Coverage (%) | Notes |
|:--|:--:|:--:|:--:|:--:|:--|
| **HumanEval_125 / DeepSeek_Checklist_k0** | Baseline | — | 45 | 0 | Initial partial coverage; no branches tested |
|  | 1 | 20 | 0 | 0 | LLM tests executed but did not trigger target paths |
|  | 2 | 10 | 0 | 0 | Still no gain; likely incorrect function calls → converged (< 3 %) |
| **HumanEval_24 / DeepSeek_CoT_k0** | Baseline | — | 50 | 0 | Some lines covered; no branch execution |
|  | 1 | 20 | 0 | 0 | Generated tests syntactically valid but ineffective |
|  | 2 | 80 | 0 | 0 | No gain despite many tests → converged (< 3 %) |

### Redundancy and De-duplication
- Many LLM-generated tests repeated identical input patterns.  
- A de-duplication filter kept **only unique** `def test_…` blocks.  
- Roughly 10–20 % of raw LLM tests were retained each iteration.

### Observations & Insights
- Coverage stagnated even after multiple iterations.  
- LLMs often guessed function names incorrectly or generated invalid inputs.  
- Despite syntactically correct tests, they did not exercise new branches.  
- This suggests that providing runtime feedback or AST-guided prompts would improve effectiveness.  


### Summary of Part 2

| Metric | HumanEval_125 | HumanEval_24 |
|:--|:--:|:--:|
| **Baseline Line Coverage (%)** | 45 | 50 |
| **Final Line Coverage (%)** | 0 | 0 |
| **Baseline Branch Coverage (%)** | 0 | 0 |
| **Final Branch Coverage (%)** | 0 | 0 |
| **Iterations Until Convergence** | 2 | 2 |

### Conclusion
LLM-assisted test generation did not increase coverage.  
Although many new tests were produced, they failed to invoke the correct functions or explore new branches.  
This underscores the need for feedback-driven generation and precise function context to achieve meaningful coverage gains.





