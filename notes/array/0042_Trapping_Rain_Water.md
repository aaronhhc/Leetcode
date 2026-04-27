# 0042 Trapping Rain Water

## Problem Idea

We are given an array `height`.

Each value represents the height of a bar.

After raining, water can be trapped between taller bars.

For each position, the trapped water depends on:

- the tallest bar on the left
- the tallest bar on the right

So the water at index `i` is:

- `min(left_max, right_max) - height[i]`

If this value is negative, it means no water is trapped there.

Example:

- `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
- answer = `6`

---

## My Code Notes

```python
water, left, right = 0, 0, len(height) - 1
left_max, right_max = height[left], height[right]

while left < right:
    if left_max < right_max:
        left += 1
        left_max = max(left_max, height[left])
        water += left_max - height[left]
    else:
        right -= 1
        right_max = max(right_max, height[right])
        water += right_max - height[right]

return water
```

What this code does:

- Use two pointers: one from the left and one from the right.
- Keep track of the highest wall seen so far from both sides.
- Always move the side with the smaller current max.
- The moved side can now safely calculate trapped water.

---

## Why Move The Smaller Max Side

At any moment:

- `left_max` is the tallest wall seen from the left
- `right_max` is the tallest wall seen from the right

The water level is limited by the smaller of these two values.

If `left_max < right_max`:

- the left side is the limiting side
- the water at the next left position depends only on `left_max`
- even if the right side changes later, it is already tall enough

So we move `left` and add:

- `left_max - height[left]`

Similarly, if `right_max <= left_max`:

- the right side is the limiting side
- we move `right` and add:

- `right_max - height[right]`

This is the key two-pointer insight.

---

## Small Example

For:

- `height = [4,2,0,3,2,5]`

Start:

- `left = 0`, `right = 5`
- `left_max = 4`, `right_max = 5`

Since `left_max < right_max`, move `left`.

At index `1`:

- `height[1] = 2`
- trapped water = `4 - 2 = 2`

Move `left` again.

At index `2`:

- `height[2] = 0`
- trapped water = `4 - 0 = 4`

Move `left` again.

At index `3`:

- `height[3] = 3`
- trapped water = `4 - 3 = 1`

Continue until the pointers meet.

Total trapped water is `9`.

---

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Why:

- Each pointer moves inward at most `n` times total.
- We only use a few variables.

---

## Key Learning

- Water at each index is controlled by the shorter boundary.
- Two pointers work because we only need to process the side with the smaller max.
- This avoids building separate prefix max and suffix max arrays.
- It gives the optimal `O(n)` time and `O(1)` space solution.
