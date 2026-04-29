# 0739 Daily Temperatures

## Problem Idea

Given a list of daily temperatures, return how many days we need to wait until a warmer temperature.

If there is no future warmer day, the answer for that day is `0`.

Example:

```text
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
answer       = [1,  1,  4,  2,  1,  1,  0,  0]
```

For day `0`, temperature is `73`.

The next warmer day is day `1`, temperature `74`, so answer is `1`.

For day `2`, temperature is `75`.

The next warmer day is day `6`, temperature `76`, so answer is `4`.

## Stack Idea

Use a stack to store indexes whose next warmer day has not been found yet.

The stack keeps temperatures in decreasing order.

For each day `i`:

- while the stack is not empty and today's temperature is warmer than the temperature at the top index
- pop that old index
- calculate how many days it waited: `i - idx`
- store that value in `res[idx]`
- push today's index into the stack

## My Code Notes

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res
```

## Why Store Indexes?

We need to know two things:

- the temperature value
- how far away the warmer day is

If we store only temperatures, we cannot calculate the distance.

So we store indexes:

```python
stack.append(i)
```

Then we can get the temperature:

```python
temperatures[stack[-1]]
```

And when we find a warmer day, we can calculate the answer:

```python
res[idx] = i - idx
```

## Walkthrough

Example:

```text
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
```

Start:

```text
res = [0, 0, 0, 0, 0, 0, 0, 0]
stack = []
```

Day `0`, temperature `73`:

```text
stack = [0]
```

Day `1`, temperature `74`:

`74` is warmer than `73`, so day `0` waited `1` day.

```text
res = [1, 0, 0, 0, 0, 0, 0, 0]
stack = [1]
```

Day `2`, temperature `75`:

`75` is warmer than `74`, so day `1` waited `1` day.

```text
res = [1, 1, 0, 0, 0, 0, 0, 0]
stack = [2]
```

Day `3`, temperature `71`:

`71` is not warmer than `75`, so just push the index.

```text
stack = [2, 3]
```

Day `4`, temperature `69`:

`69` is not warmer than `71`, so just push the index.

```text
stack = [2, 3, 4]
```

Day `5`, temperature `72`:

`72` is warmer than `69`, so day `4` waited `1` day.

`72` is also warmer than `71`, so day `3` waited `2` days.

```text
res = [1, 1, 0, 2, 1, 0, 0, 0]
stack = [2, 5]
```

Day `6`, temperature `76`:

`76` is warmer than `72`, so day `5` waited `1` day.

`76` is also warmer than `75`, so day `2` waited `4` days.

```text
res = [1, 1, 4, 2, 1, 1, 0, 0]
stack = [6]
```

Day `7`, temperature `73`:

`73` is not warmer than `76`, so just push the index.

```text
stack = [6, 7]
```

The remaining indexes in the stack have no future warmer day, so their answers stay `0`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

Why:

- Each index is pushed into the stack once.
- Each index is popped from the stack at most once.
- The result array and stack both can use up to `n` space.
