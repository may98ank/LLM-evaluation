# Evaluation of Code Generation Strategies with Locally Running LLMs


## 1. Experimental Setup
- **Dataset:** HumanEvalPlus (10 tasks)
- **Platform:** macOS + Ollama
- **Models (Families):** Qwen (`qwen2.5-coder:3b`), DeepSeek (`deepseek-coder:1.3b`)
- **Strategies:** Chain-of-Thought (CoT), Checklist (innovation), Self-Repair (for failures)
- **Metric:** pass@k with k=3, temperature=0.2

## 2. Global Results

| strategy   | family   |   mean_pass@k |
|------------|----------|---------------|
| Checklist  | DeepSeek |           0.9 |
| Checklist  | Qwen     |           1   |
| CoT        | DeepSeek |           0.6 |
| CoT        | Qwen     |           1   |

## 3. Per-Task Results

#### Task: `101`

| family   | strategy   |   k |   passes |   pass@k |
|----------|------------|-----|----------|----------|
| DeepSeek | Checklist  |   3 |        2 |        1 |
| DeepSeek | CoT        |   3 |        3 |        1 |
| Qwen     | Checklist  |   3 |        3 |        1 |
| Qwen     | CoT        |   3 |        2 |        1 |

#### Task: `25`

| family   | strategy    |   k |   passes |   pass@k |
|----------|-------------|-----|----------|----------|
| DeepSeek | Checklist   |   3 |        1 |        1 |
| DeepSeek | CoT         |   3 |        0 |        0 |
| DeepSeek | Self-Repair |   1 |        0 |        0 |
| Qwen     | Checklist   |   3 |        3 |        1 |
| Qwen     | CoT         |   3 |        3 |        1 |

#### Task: `134`

| family   | strategy   |   k |   passes |   pass@k |
|----------|------------|-----|----------|----------|
| DeepSeek | Checklist  |   3 |        2 |        1 |
| DeepSeek | CoT        |   3 |        1 |        1 |
| Qwen     | Checklist  |   3 |        3 |        1 |
| Qwen     | CoT        |   3 |        2 |        1 |

#### Task: `145`

| family   | strategy    |   k |   passes |   pass@k |
|----------|-------------|-----|----------|----------|
| DeepSeek | Checklist   |   3 |        0 |        0 |
| DeepSeek | CoT         |   3 |        0 |        0 |
| DeepSeek | Self-Repair |   1 |        0 |        0 |
| Qwen     | Checklist   |   3 |        3 |        1 |
| Qwen     | CoT         |   3 |        3 |        1 |

#### Task: `147`

| family   | strategy   |   k |   passes |   pass@k |
|----------|------------|-----|----------|----------|
| DeepSeek | Checklist  |   3 |        1 |        1 |
| DeepSeek | CoT        |   3 |        0 |        0 |
| Qwen     | Checklist  |   3 |        3 |        1 |
| Qwen     | CoT        |   3 |        3 |        1 |

#### Task: `24`

| family   | strategy   |   k |   passes |   pass@k |
|----------|------------|-----|----------|----------|
| DeepSeek | Checklist  |   3 |        2 |        1 |
| DeepSeek | CoT        |   3 |        3 |        1 |
| Qwen     | Checklist  |   3 |        3 |        1 |
| Qwen     | CoT        |   3 |        3 |        1 |

#### Task: `50`

| family   | strategy   |   k |   passes |   pass@k |
|----------|------------|-----|----------|----------|
| DeepSeek | Checklist  |   3 |        2 |        1 |
| DeepSeek | CoT        |   3 |        0 |        0 |
| Qwen     | Checklist  |   3 |        3 |        1 |
| Qwen     | CoT        |   3 |        3 |        1 |

#### Task: `51`

| family   | strategy   |   k |   passes |   pass@k |
|----------|------------|-----|----------|----------|
| DeepSeek | Checklist  |   3 |        3 |        1 |
| DeepSeek | CoT        |   3 |        3 |        1 |
| Qwen     | Checklist  |   3 |        3 |        1 |
| Qwen     | CoT        |   3 |        3 |        1 |

#### Task: `52`

| family   | strategy   |   k |   passes |   pass@k |
|----------|------------|-----|----------|----------|
| DeepSeek | Checklist  |   3 |        2 |        1 |
| DeepSeek | CoT        |   3 |        2 |        1 |
| Qwen     | Checklist  |   3 |        3 |        1 |
| Qwen     | CoT        |   3 |        3 |        1 |

#### Task: `66`

| family   | strategy   |   k |   passes |   pass@k |
|----------|------------|-----|----------|----------|
| DeepSeek | Checklist  |   3 |        1 |        1 |
| DeepSeek | CoT        |   3 |        3 |        1 |
| Qwen     | Checklist  |   3 |        3 |        1 |
| Qwen     | CoT        |   3 |        3 |        1 |

## 4. Failure & Self-Repair Cases
| task_id       | original_strategy   | family   |   repair_pass@k |
|---------------|---------------------|----------|-----------------|
| 125 | CoT                 | DeepSeek |               0 |
| 145 | Checklist           | DeepSeek |               0 |

`repair_pass@k = 1` means the self-repair attempt generated at-least one passing solution.


## 5. Innovation: Checklist Prompt
**Logic:** Tells models to list down all edge cases before start working on coding, then delete the checklist and return only the runnable code.

**Observation:** There was a increase in pass@k vs CoT by adding explicit handling of boundary conditions.


## 6. Reproducibility
- **Models:** qwen2.5-coder:3b, deepseek-coder:1.3b
- **Dataset:** evalplus/humanevalplus
- **Params:** tasks=10, k=3, temperature=0.2
- **Files produced:** 
  - `results/results_attempts.csv`
  - `results/results_pass_at_k.csv`
  - `results/results_prompts.jsonl`
  - `generated-code/` (all generations, organized)

## Original 10 Problem Prompts

### HumanEval/66

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).


def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
```

### HumanEval/101

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).


def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
```

### HumanEval/125

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).


def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
```

### HumanEval/147

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).


def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
```

### HumanEval/145

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).


def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
```

### HumanEval/24

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).



def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
```

### HumanEval/51

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).



def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
```

### HumanEval/134

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).


def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
```

### HumanEval/50

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).



def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
```

### HumanEval/52

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).



def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
```

## Example Generated Code Snippets

### HumanEval/52 — Qwen / CoT (k=0)
```python
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # Check if the list is empty or has only one element
    if not l:
        return True
    
    # Iterate over each element in the list
    for num in l:
        # If any number is not below the threshold, return False
        if num >= t:
            return False
    
    # If all numbers are below the threshold, return True
    return True
```

### HumanEval/24 — DeepSeek / CoT (k=2)
```python
def largest_divisor(n: int) -> str : #changed the function's type hint from 'int'->str, as we want to output a string not an integer in our case 
    """ For given input n find all factors of that number and return maximum factor. This is tricky part will be ignored for final implementation but here it serves purpose."""  
    
    # Initialize the list with first divisor which would always equal '1' as per definition, no need to check further 
    largest_divisors = [i for i in range(2 , int(n**0.5) + 1 ) if n % i == 0 ]  
    
    # Append the larger factors after finding smaller ones because a number can have more than one divisor, so we need to find all of them 
    largest_divisors += [i for i in range(largest_divisors[-1] , int(n/2) + 1 , -1 ) if n % i == 0 ]  
    
    # Return the maximum divisor found. If there is no such number, return 'None' 
    largest = max(largest_divisors or [0])     
        
    print("Largest Divisible Number: ", int(n) if n % (1 + largest ) == 0 else "No Larger divisor found") #prints the number only when it's a valid result, otherwise prints 'None'.  This is to make sure we are not returning an empty string or None.
    return str(largest_divis
```

### HumanEval/24 — DeepSeek / CoT (k=0)
```python
def largest_divisor(n):   # Step-by step explanation of the problem statement here, then output only final python implementation  (no prose or tests) .
    """ For a given number n , find out which is smallest divisible integer that can divide evenly into 'N' and less than N. If there are no such integers return -1 as per requirement."""   # Step-by step explanation of the problem statement here, then output only final python implementation  (no prose or tests) .
    
    i = n // 2 + 1        # Start from one more than half to check for even divisibility. This is because all numbers can be divided by two and there's no need of checking if the number itself could divide into 'N'.   (no prose or tests) .
    
    while i > 0:           # Step-by step explanation here, then output only final python implementation  (no prose). This loop will run until it finds a divisor. If no such integer is found return -1 as per requirement.(No Prose/Tests required.)   No tests are written for this part of the code in Python programming language
        if n % i == 0:     # Step-by step explanation here, then output only final python implementation  (no prose). This condition checks whether 'i' is
```

### HumanEval/24 — Qwen / Checklist (k=2)
```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test cases
assert largest_divisor(15) == 5
assert largest_divisor(28) == 14
assert largest_divisor(37) == 1  # 37 is a prime number
```
