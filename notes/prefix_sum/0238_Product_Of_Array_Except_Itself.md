# 0238. Product of Array Except Self

## Idea

For each index, we want:

- the product of all numbers on the left, prefix
- multiplied by the product of all numbers on the right, suffix

So we do it in two passes:

1. left to right: store the prefix product in `ans[i]`
2. right to left: multiply the suffix product into `ans[i]`

## Key Insight

Instead of computing the product for each index separately,  
we reuse previous results.

For each position:

- `prefix` = product of all elements before `i`
- `suffix` = product of all elements after `i`

So:

`answer[i] = prefix[i] * suffix[i]`

## Why this works

In the first pass:

- `ans[i]` stores the product of everything to the left of `i`

In the second pass:

- multiply by the product of everything to the right of `i`

That gives the product of all elements except itself.

## Example

For `nums = [1, 2, 3, 4]`

After prefix pass:

`ans = [1, 1, 2, 6]`

After suffix pass:

`ans = [24, 12, 8, 6]`

## Complexity

- Time: `O(n)`
- Space: `O(1)` extra space  
  (not counting the output array)

## Note

This solution avoids division and is the optimal approach.

The key idea is:

- first store left product
- then multiply right product
- combine both in the same output array
- `for i in range(n-1, -1, -1)` iterate from the ass