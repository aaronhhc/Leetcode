# LeetCode 134. Gas Station

There are `n` gas stations arranged in a circle.

- `gas[i]`: the amount of gas available at station `i`
- `cost[i]`: the amount of gas needed to travel from station `i` to the next station
- Return the starting station index if we can complete the circuit
- Return `-1` if no valid starting station exists

## 1. My initial approach

My first idea was to use brute force:

- Try every station as a possible starting point
- Simulate the entire circular route
- Check whether the tank ever becomes negative

This approach is logically correct, but its worst-case time complexity is `O(n²)`.

The important question is:

> When one starting point fails, can we eliminate other starting points at the same time?

## 2. The key greedy observation

Suppose we start from `start` and reach station `i`, but the tank becomes negative:

```python
tank < 0
```

This means the total gas from `start` to `i` is not enough to cover the total cost.

At first, we only know that `start` is invalid. However, every station between `start` and `i` is also invalid.

Why?

Before reaching `i`, the accumulated tank from `start` never became negative. If we start from any station in the middle, we lose the gas accumulated before that station. Therefore, reaching `i` would be even worse.

So we can eliminate all of them and set:

```python
start = i + 1
```

This is the main greedy step.

## 3. Why I cannot use `break`

My first attempt stopped when the current route failed:

```python
if total < 0:
    total = 0
    break
```

This is incorrect because a local failure does not necessarily mean that the whole problem has no solution.

A failure only means:

> The current candidate starting range is invalid. Continue searching from `i + 1`.

The entire problem is impossible only when the total gas is less than the total cost.

## 4. `tank` and `total` have different meanings

It was initially confusing because both variables accumulate `gas[i] - cost[i]`.

### `tank`

```python
tank += gain
```

- Represents the current gas balance from the current candidate `start`
- Used to determine whether the current candidate can continue
- Must be reset when we choose a new starting point

### `total`

```python
total += gain
```

- Represents the total gas balance across the entire array
- Used to determine whether completing the whole circuit is possible
- Must not be reset when `tank` is reset

The two variables track different scopes:

```text
tank  -> current candidate route
total -> entire circular route
```

## 5. Why `tank` must be reset

When `tank < 0`, we abandon the old starting point:

```python
start = i + 1
tank = 0
```

The new candidate starts at `i + 1`, so the gas accumulated from the old candidate must not be carried over.

However, `total` still represents the complete array, so it continues accumulating normally.

This is why:

- Reset `tank`
- Do not reset `total`

## 6. Handling the impossible case

Even if the greedy scan finds a candidate `start`, the entire circuit may still be impossible.

We must check:

```python
total >= 0
```

If:

```python
total < 0
```

then:

```text
sum(gas) < sum(cost)
```

The total amount of gas in the entire circuit is insufficient, so no starting point can work.

## 7. Why one pass is enough for a circular route

At first, it may seem strange that the code only scans from index `0` to `n - 1`, because the route is circular.

We do not need to explicitly simulate:

```text
start -> ... -> n - 1 -> 0 -> ... -> start - 1
```

The one-pass greedy scan finds the only possible candidate starting point after eliminating all failed candidates.

Then:

- `total >= 0` guarantees that the total gas is enough for the complete circuit
- `tank` guarantees that the candidate can reach the end of the linear scan
- Together, they guarantee that the candidate can also continue from `n - 1` back to `0` and finish the circuit

Therefore, one pass is sufficient.

## 8. Clean Python solution

```python
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = 0
        tank = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]

            total += gain
            tank += gain

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1
```

## 9. Trace example

```python
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
```

The net gains are:

```text
[-2, -2, -2, 3, 3]
```

| Station | Gain | Total | Tank | Start |
| --- | ---: | ---: | ---: | ---: |
| 0 | -2 | -2 | -2 | 1 |
| 1 | -2 | -4 | -2 | 2 |
| 2 | -2 | -6 | -2 | 3 |
| 3 | 3 | -3 | 3 | 3 |
| 4 | 3 | 0 | 6 | 3 |

At the end:

```text
total = 0
start = 3
```

Therefore, the answer is:

```text
3
```

## 10. The core invariant

During the scan:

- `total` is the total net gain from all processed stations
- `tank` is the net gain from the current candidate `start`
- If `tank < 0` at station `i`, every station from the old `start` through `i` can be eliminated
- The next possible candidate is `i + 1`

## 11. Complexity

- Time complexity: `O(n)`
- Space complexity: `O(1)`

The initial `diff` array is unnecessary:

```python
diff[i] = gas[i] - cost[i]
```

We can calculate the gain during the scan instead:

```python
gain = gas[i] - cost[i]
```

This keeps the solution at constant extra space.

## 12. My main takeaways

The three most important ideas in this problem are:

1. **Why can `tank < 0` skip directly to `i + 1`?**

   Because every station between the old `start` and `i` would have even less accumulated gas and must also fail.

2. **Why reset `tank` but not `total`?**

   Because `tank` belongs to the current candidate start, while `total` represents the entire route.

3. **Why is one linear scan enough for a circular route?**

   The greedy scan finds the only possible candidate, and `total >= 0` guarantees that the candidate can complete the remaining circular route.

## 13. Common mistakes

- Trying every starting point with brute force and getting `O(n²)`
- Thinking a local failure means the entire problem has no solution
- Using `break` instead of continuing from `i + 1`
- Resetting `total` together with `tank`
- Forgetting to check `total >= 0`
- Creating an unnecessary `diff` array
- Forgetting that the route is circular
- Forgetting to import `List` when using the type annotation
