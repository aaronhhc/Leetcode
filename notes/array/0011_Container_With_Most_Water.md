# 0011 Container With Most Water

## Problem Idea

We are given an array `height`.

Each value represents a vertical line on the x-axis.

We pick two lines, and those two lines plus the x-axis form a container.

The amount of water this container can hold is:

- `width * min(left_height, right_height)`

Example:

- `height = [1,8,6,2,5,4,8,3,7]`
- choose lines at index `1` and index `8`
- width = `8 - 1 = 7`
- height = `min(8, 7) = 7`
- area = `7 * 7 = 49`

The goal is to find the maximum possible area.

---

## My Code Notes

```python
left, right = 0, len(height) - 1
most_water = 0

while(left < right):
    curr_most_water = (right - left) * min(height[left], height[right])
    most_water = max(curr_most_water, most_water)

    if height[left] <= height[right]:
        left += 1
    else:
        right -= 1

return most_water
```

What this code does:

- Start with two pointers at the far left and far right.
- Compute the current container area.
- Update the best answer seen so far.
- Move the pointer that has the shorter height inward.

---

## Why Move The Shorter Side

The area is determined by:

- width: `right - left`
- height: `min(height[left], height[right])`

When we move a pointer inward:

- the width always becomes smaller

So if we want a better area, we need a chance to increase the limiting height.

If `height[left] <= height[right]`:

- the left side is the bottleneck
- moving `right` inward would only reduce width, while the height limit still cannot exceed `height[left]`
- so the only useful move is `left += 1`

Similarly, if `height[right] < height[left]`:

- the right side is the bottleneck
- so we move `right -= 1`

This is the key greedy idea in the problem.

---

## Small Example

For:

- `height = [1,8,6,2,5,4,8,3,7]`

Start:

- `left = 0`, `right = 8`
- area = `(8 - 0) * min(1, 7) = 8`

Since `1 < 7`, move `left` forward.

Now:

- `left = 1`, `right = 8`
- area = `(8 - 1) * min(8, 7) = 49`

This becomes the best answer.

The pointers keep moving inward until they meet.

---

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Why:

- Each pointer moves at most `n` times.
- No extra data structure is used.

---

## Key Learning

- This is a classic two-pointer problem.
- The container height is limited by the shorter line.
- To search for a better answer, move the shorter side inward.
- Even though the width shrinks, we may find a taller limiting side and get a larger area.
