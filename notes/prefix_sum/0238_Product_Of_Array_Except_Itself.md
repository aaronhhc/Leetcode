# 0238. Product of Array Except Self

## Problem Idea

For every index `i`, return the product of every element except `nums[i]`.

Division is not allowed, so split the product into two parts:

```text
answer[i] = product of elements to the left of i
            * product of elements to the right of i
```

## Two-Pass Approach

Set `res = [1] * n`, then use the output array to store the left products first.

### 1. Prefix pass: left to right

Before processing `i`, `res[i - 1]` contains the product of all elements before `i - 1`.
Therefore:

```python
res[i] = res[i - 1] * nums[i - 1]
```

After this pass, `res[i]` is the product of everything to the left of `i`.

### 2. Suffix pass: right to left

Maintain `suffix`, the product of all elements to the right of the current index.
For each index:

```python
res[i] *= suffix
suffix *= nums[i]
```

The first line completes the answer for `i`; the second line updates the suffix product for the next index.

After the reverse pass, return `res`. Both passes use the same array, so no separate prefix or suffix array is needed.

## Example

For `nums = [1, 2, 3, 4]`:

After the prefix pass:

```text
res = [1, 1, 2, 6]
```

After the suffix pass:

```text
res = [24, 12, 8, 6]
```

The same approach also handles zero values naturally. For example, `[1, 2, 0, 4]` produces `[0, 0, 8, 0]` without any special cases.

## Why This Works

At every index, `res[i]` starts as the product of all elements before `i`. The suffix pass multiplies it by the product of all elements after `i`, so the current element is never included.

The output array replaces a separate prefix array, which keeps the extra space constant.

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`, excluding the output array

## Key Learning

- Build left products in the output array.
- Traverse from right to left to multiply in right products.
- The initial value `1` represents the empty product at either end.
- `range(n - 1, -1, -1)` iterates backward from the last index to `0`.