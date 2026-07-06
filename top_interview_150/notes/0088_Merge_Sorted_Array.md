# 0088 Merge Sorted Array

## Problem Idea

We are given two sorted arrays:

- `nums1` contains `m` valid values followed by `n` empty positions.
- `nums2` contains `n` valid values.

The goal is to merge `nums2` into `nums1` in non-decreasing order.

The result must be stored directly in `nums1`.

---

## My Approach

Use three pointers and fill `nums1` from right to left:

- `i` points to the last valid value in `nums1`.
- `j` points to the last value in `nums2`.
- `k` points to the last available position in `nums1`.

```python
i = m - 1
j = n - 1
k = m + n - 1
```

At each step, compare `nums1[i]` and `nums2[j]`.

Place the larger value at `nums1[k]`, then move the corresponding pointer and
`k` one position to the left.

```python
while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1
```

---

## Why Merge From the End?

If we merge from the beginning, writing a value into `nums1` could overwrite a
valid value that has not been compared yet.

The empty positions are at the end of `nums1`, so filling from right to left lets
us safely place the largest remaining value without losing data.

---

## Important Mistakes

### 1. Merging from the front

Writing from the beginning of `nums1` can overwrite valid values before they
have been compared.

For example:

```text
nums1 = [2, 4, 0, 0]
nums2 = [1, 3]
```

If `1` is written at index `0`, the value `2` is lost unless it was saved
somewhere else. Merging backwards avoids this problem because the writable
positions at the end of `nums1` are empty.

### 2. Using `nums1.insert()`

`insert()` shifts all later elements to the right, so one insertion can take
`O(m + n)` time. Repeating it can make the full solution `O((m + n)^2)`.

It is also unnecessary because `nums1` already has enough space for every
value. The three-pointer solution writes directly into that space.

### 3. Writing `nums1 = nums2`

This only changes what the local variable `nums1` refers to. It does not modify
the original list that was passed into the function.

```python
nums1 = nums2  # Rebinds the local name; not an in-place modification
```

LeetCode checks the original `nums1` list after the method finishes, so its
elements must be changed directly, such as with `nums1[k] = value`.

### 4. Forgetting the remaining `nums2` values

The main loop stops as soon as either array has no values left to compare. If
`nums2` still has values, they are smaller than everything already placed at the
back and must be copied into the front of `nums1`.

```python
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1
```

Without this loop, a case such as the following would be incorrect:

```text
nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]
```

### 5. Copying the remaining `nums1` values

If `nums2` is exhausted first, the remaining values in `nums1` are already in
their correct positions. Copying them would do nothing, so a second cleanup loop
for `nums1` is not needed.

---

## Remaining Values

After the main loop, there are two possibilities.

### Values remain in `nums2`

They must be copied into the remaining positions in `nums1`:

```python
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1
```

### Values remain in `nums1`

Nothing needs to be done because those values are already in their correct
positions.

This is why the code only needs a cleanup loop for `nums2`.

---

## Small Example

```text
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6],          n = 3
```

Start with:

```text
i = 2 -> nums1[i] = 3
j = 2 -> nums2[j] = 6
k = 5
```

The values placed from right to left are:

```text
6, 5, 3, 2, 2, 1
```

Final result:

```text
nums1 = [1, 2, 2, 3, 5, 6]
```

---

## Complexity

- Time: `O(m + n)`
- Extra space: `O(1)`

Each valid value is processed at most once, and the merge is performed directly
inside `nums1`.

---

## Key Learning

- When an array has empty space at the end, consider filling it backwards.
- Use three pointers to track both input arrays and the write position.
- Put the larger value at the back first.
- Only leftover values from `nums2` need to be copied.
