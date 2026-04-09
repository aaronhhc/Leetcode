# 0167 Two Sum II - Input Array Is Sorted

## Problem Idea

We are given:

- a sorted array `numbers`
- a target value `target`

We need to find two numbers that add up to `target` and return their positions.

Important detail:

- the answer must be returned as `1-indexed`
- the array is already sorted

Example:

- `numbers = [2, 7, 11, 15]`
- `target = 9`
- `2 + 7 = 9`
- answer: `[1, 2]`

Because the array is sorted, this problem is a classic two-pointer question.

---

## My Code Notes

### 1. Self-written hash map solution

```python
num_dict = defaultdict(int)
n = len(numbers)
for i in range(n):
    com = target - numbers[i]
    if com in num_dict:
        return [min(i + 1, num_dict[com] + 1), max(i + 1, num_dict[com] + 1)]
    num_dict[numbers[i]] = i
```

What this version does:

- For each number, compute the complement:
  `com = target - numbers[i]`
- Check whether that complement has already appeared.
- If yes, return the two indices.
- If not, store the current number and its index in the dictionary.

Why it works:

- If `numbers[i] + com = target`
- and `com` was seen earlier
- then we found a valid pair

One small detail:

- the problem wants `1-indexed` positions
- so the code returns `i + 1`

The `min(...)` and `max(...)` are used to make sure the smaller index comes first.

---

### 2. Two-pointer solution

```python
left = 0
right = len(numbers) - 1
while(left < right):
    cur_total = numbers[left] + numbers[right]
    if target > cur_total:
        left += 1
    elif target < cur_total:
        right -= 1
    else:
        return [left + 1, right + 1]
```

What this version does:

- `left` starts from the smallest value
- `right` starts from the largest value
- add the two values together
- move one pointer depending on whether the sum is too small or too large

Pointer movement logic:

- If `cur_total < target`, move `left` rightward to increase the sum.
- If `cur_total > target`, move `right` leftward to decrease the sum.
- If `cur_total == target`, return the answer.

This works especially well because the array is sorted.

---

## Why Two Pointers Work

Suppose:

- `numbers[left] + numbers[right] < target`

Since the array is sorted:

- moving `right` left would make the sum smaller
- that will not help us reach `target`
- so we should move `left` forward

Now suppose:

- `numbers[left] + numbers[right] > target`

Then:

- moving `left` right would make the sum even larger
- so we should move `right` backward

Because every move removes impossible cases, we can solve the problem in one pass.

---

## Key Python Concepts

### Dictionary lookup

In the first solution:

- `num_dict[numbers[i]] = i`

stores a number and its index.

Then:

- `if com in num_dict`

checks whether the matching value was seen before.

This is the same core idea as regular Two Sum.

---

### 1-indexed answer

Python lists use `0-indexed` positions, but the problem wants `1-indexed` positions.

So:

- index `0` becomes `1`
- index `1` becomes `2`

That is why both solutions return:

- `left + 1`
- `right + 1`

or the equivalent adjusted indices in the hash map version.

---

## Complexity

### Hash map solution

- Time: `O(n)`
- Space: `O(n)`

Why:

- We scan the array once.
- The dictionary may store up to `n` elements.

### Two-pointer solution

- Time: `O(n)`
- Space: `O(1)`

Why:

- Each pointer only moves inward.
- No extra data structure is needed.

---

## Key Learning

- This problem is very similar to `Two Sum`, but the sorted array changes the best approach.
- A hash map solution still works.
- But the two-pointer solution is cleaner and uses less space.
- When an array is sorted, always consider whether two pointers can replace a hash map.
