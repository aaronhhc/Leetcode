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
