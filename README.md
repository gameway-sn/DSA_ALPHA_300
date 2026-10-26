# SRM Alpha 300 · Category B · DSA Placement Training Repository

This repository contains daily solutions for the **SRM Alpha 300 (Category B)** placement training DSA plan across **October, November, and December 2026**.

---

## 📁 Repository Folder Structure

The repository follows a standardized lowercase-hyphenated hierarchy:

```text
Alpha300/
├── <month>/
│   └── <week>/
│       └── <month-date>/
│           ├── problem_1_<name>.py
│           ├── problem_2_<name>.py
│           ├── problem_3_<name>.py
│           └── README.md
```

### Example:
For problem solutions on **22nd October**:
```text
oct/week-4/22-oct/
├── problem_1_binary_search.py
├── problem_2_search_insert_position.py
├── problem_3_first_bad_version.py
└── README.md
```

---

## 📜 Daily Rules & Program Guidelines

### 1. Daily Rhythm
- **3 problems per day** solved unaided in Python.
- Pushed to your personal GitHub repository by midnight IST.
- Discord submission command:
  ```text
  /done day{N} <github_link_1> <github_link_2> <github_link_3>
  ```
- Streak counts only when all 3 problems are logged by midnight.

### 2. The No-Libraries Rule (Primitives Only)
Every data structure must be built from primitives. Using shortcuts defeats the purpose of the exercise.
- **Allowed Primitives:**
  - `list` (array methods: `.append()`, `.pop()`, `[i]`, `len()`)
  - `dict` (custom hashmap: `.get(k, 0)`, direct key lookup/assignment)
  - `set` (hashset)
  - `int`, `float`, `str`, `tuple`, `bool`
  - Basic string methods: `.isalnum()`, `.lower()`, `.split()`, `ch.isalpha()`, `ord()`, `chr()`
- **Forbidden Shortcuts (Cold List Triggers):**
  - ❌ `collections.deque` (build doubly linked list from scratch)
  - ❌ `collections.Counter` (build frequency dictionaries manually)
  - ❌ `collections.defaultdict`
  - ❌ `collections.OrderedDict`
  - ❌ `heapq`
  - ❌ `bisect`, `bisect_left`, `bisect_right` (write manual binary search)
  - ❌ `itertools.accumulate`, `takewhile`, `groupby`
  - ❌ `functools.lru_cache`, `reduce`
  - ❌ `sorted()` / `list.sort()` (forbidden until implementing sort algorithms yourself)
  - ❌ `s[::-1]` / `reversed()` (write the reversal loop manually)

### 3. README Per Problem / Day Format
Each folder contains a `README.md` documenting:
1. **Approach** (2–3 lines)
2. **Time & Space Complexity**
3. **One Edge Case Missed on First Attempt**
4. **Discord Verification Command**

---

## 🗓️ 3-Month Curriculum Overview

| Month | Topic | Key Focus | Total Problems |
| :--- | :--- | :--- | :--- |
| **`oct/`** | **Arrays + Sorting + Binary Search** | Traversals, prefix sum, two pointers, sliding window, custom sorting algorithms, binary search variants. | 90 problems |
| **`nov/`** | **Strings** | Manipulations, manual frequency counting, palindromes, sliding window, pattern matching, encoding. | 87 problems |
| **`dec/`** | **Linked Lists** | Singly, Doubly, and Circular linked lists from scratch, LRU cache, list sorting, K-group reversals. | 90 problems |

For complete day-by-day problem specifications, topics, and restrictions, refer to [`curriculum_mapping.json`](curriculum_mapping.json).
