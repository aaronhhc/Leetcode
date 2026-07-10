# LeetCode 189: Rotate Array

## Problem
Given an integer array `nums`, rotate the array to the right by `k` steps in-place.

---

## 1. My initial idea and why it causes TLE

My first thought was to rotate the array one step at a time, repeating this `k` times.

- For each step, I would move every element one position to the right.
- That means each step costs `O(n)` work.
- Repeating `k` steps makes the total cost `O(n * k)`.

Why this is too slow:

- When `k` is large, `n * k` can become very large.
- For example, if `n = 10^5` and `k = 10^5`, this becomes `10^10` operations.
- This is far too slow for LeetCode time limits.

So the key mistake was simulating each rotation instead of computing the final arrangement directly.

---

## 2. Key observation

Do not simulate every rotation.

Right rotating by `k` means:

- the last `k` elements move to the front
- the first `n - k` elements move to the back

Example:

- Original: `[1, 2, 3, 4, 5, 6, 7]`
- `k = 3`
- Result: `[5, 6, 7, 1, 2, 3, 4]`

This is the final structure we want, and we should build it without repeated shifting.

---

## 3. Important detail: normalize `k`

Before doing any index-based operations, normalize `k` with `k %= n`.

Why this is needed:

- Rotating by `n` steps returns the array to the same position.
- Rotating by `k` steps is equivalent to rotating by `k % n` steps.

Example:

- `[1, 2, 3]`, rotating by `4` steps is the same as rotating by `1` step.
- Without `k %= n`, code may try to use incorrect ranges like `k - 1` or `k` when `k > n`.
- That can cause wrong index decisions or invalid ranges.

So always do:

```python
k %= n
```

---

## 4. In-place reverse solution

The clean solution uses three reversals.

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n - k` elements.

Trace with example:

- Original: `[1, 2, 3, 4, 5, 6, 7]`
- After reverse all: `[7, 6, 5, 4, 3, 2, 1]`
- After reverse first `k`: `[5, 6, 7, 4, 3, 2, 1]`
- After reverse rest: `[5, 6, 7, 1, 2, 3, 4]`

Why this works:

- After the full reverse, the last `k` elements are at the front but in reverse order.
- Reversing the first `k` elements restores their order.
- Reversing the remaining `n - k` elements restores the rest.

---

## 5. Python implementation

Python allows a nested helper function and closure over `nums`.

- Define a local `reverse(left, right)` helper inside `rotate`.
- The helper can access `nums` from the outer function because of Python closure rules.
- This keeps the code compact and readable.

---

## 6. C++ implementation

C++ does not allow normal nested functions inside another function.

Two valid alternatives:

- use a private helper function
- use a lambda

The recommended solution is a private helper function.

- C++ has built-in `swap`, usually available as `std::swap`.
- LeetCode often allows `swap(...)` directly because `using namespace std` is often in effect.

---

## 7. Complexity

- Time complexity: `O(n)`
- Space complexity: `O(1)`

The helper only swaps elements in-place, so no extra array is needed.

---

## 8. Common mistakes and what to improve

- I initially simulated every rotation instead of transforming the array directly.
- I forgot that `k` can be larger than `n`.
- I need to remember that `n` is the length, while `n - 1` is the last index.
- I need to practice recognizing when reverse can solve array rearrangement problems.
- I transferred Python nested function style directly to C++, but C++ requires a helper function or lambda.
- I should use `swap` in C++ instead of manually writing a temp variable when appropriate.

This note captures the right way to think about the problem and avoid the common pitfalls.