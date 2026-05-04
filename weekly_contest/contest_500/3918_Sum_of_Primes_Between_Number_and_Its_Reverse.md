# 3918 Sum of Primes Between Number and Its Reverse

## Problem Idea

Given an integer `n`, reverse its digits first.

Then look at the inclusive range between:

```text
n and reverse(n)
```

Return the sum of all prime numbers inside that range.

Example:

```text
n = 31
reverse(n) = 13

range = [13, 14, 15, ..., 31]
prime numbers = 13, 17, 19, 23, 29, 31
answer = 132
```

Because `n` can be larger or smaller than its reverse, we should use:

```python
min(n, reverse), max(n, reverse)
```

## My First Idea

My first solution does two things:

1. Reverse `n` by converting it to a string.
2. Check every number in the range and add it if it is prime.

The reverse part:

```python
reverse = int(str(n)[::-1])
```

This is a clean Python way to reverse digits.

For example:

```text
120 -> "120" -> "021" -> 21
```

The leading zero disappears after converting back to `int`, which is correct for a number.

## Prime Check

The helper function:

```python
def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for d in range(3, int(n ** 0.5) + 1, 2):
        if n % d == 0:
            return False

    return True
```

This is a standard trial division prime check.

Important details:

- `n <= 1` is not prime.
- `2` is prime.
- Other even numbers are not prime.
- After removing even numbers, only test odd divisors.
- Only test up to `sqrt(n)`.

Why only test up to `sqrt(n)`?

If `n` has a factor larger than `sqrt(n)`, then the matching factor must be smaller than `sqrt(n)`.

Example:

```text
36 = 4 * 9
```

Once we test up to `6`, we already know whether there is a factor pair.

## Is My First Solution Standard?

Yes, this is a standard solution for a single-number range problem.

It is especially reasonable because:

- the logic is easy to understand
- the prime check is written correctly
- checking only odd divisors makes it faster than checking every divisor
- using `min` and `max` handles both directions of the range

The only thing I would change for Python style is the function name:

```python
isPrime
```

could become:

```python
is_prime
```

But algorithmically, this version is fine.

## My First Code Notes

```python
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def isPrime(n: int) -> bool:
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False

            for d in range(3, int(n ** 0.5) + 1, 2):
                if n % d == 0:
                    return False

            return True
            
        res = 0
        reverse = int(str(n)[::-1])
        for i in range(min(n, reverse), max(n, reverse) + 1):
            if isPrime(i):
                res += i
        return res
```

What this code does:

- `reverse = int(str(n)[::-1])` gets the reversed number.
- `min(n, reverse)` is the start of the range.
- `max(n, reverse)` is the end of the range.
- For every number in the range, call `isPrime`.
- If it is prime, add it to `res`.

## Sieve Version

Your current file also has a Sieve of Eratosthenes version:

```python
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        reverse = int(str(n)[::-1])

        left = min(n, reverse)
        right = max(n, reverse)

        is_prime = [True] * (right + 1)

        if right >= 0:
            is_prime[0] = False
        if right >= 1:
            is_prime[1] = False

        for p in range(2, int(right ** 0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, right + 1, p):
                    is_prime[multiple] = False

        res = 0
        for x in range(left, right + 1):
            if is_prime[x]:
                res += x

        return res
```

This is also standard.

The idea is:

- first mark every number from `0` to `right` as possibly prime
- manually mark `0` and `1` as not prime
- for every prime `p`, mark its multiples as not prime
- finally sum the prime numbers from `left` to `right`

The key line is:

```python
for multiple in range(p * p, right + 1, p):
```

Why start from `p * p`?

Because smaller multiples of `p` were already marked by smaller factors.

Example:

```text
p = 5

10 was already marked by 2
15 was already marked by 3
20 was already marked by 2

So 5 can start marking from 25
```

## Important Python Note

In your current `.py` file, there are two `class Solution` definitions:

```python
class Solution:
    ...

class Solution:
    ...
```

Python keeps the second one.

So the version that actually runs on LeetCode is the sieve version, not the first trial division version.

This is acceptable if you intentionally want to keep both for learning, but it can be confusing when rereading the file.

A cleaner practice is:

```python
class TrialDivisionSolution:
    ...

class Solution:
    ...
```

That way:

- your first idea is still saved
- LeetCode still uses `class Solution`
- it is clear which version is the final answer

## Clean Version

If you want to submit the trial division idea, this is a cleaner version with a more Python-style helper name and named range boundaries:

```python
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x <= 1:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False

            for d in range(3, int(x ** 0.5) + 1, 2):
                if x % d == 0:
                    return False

            return True

        rev = int(str(n)[::-1])
        start = min(n, rev)
        end = max(n, rev)

        total = 0
        for x in range(start, end + 1):
            if is_prime(x):
                total += x

        return total
```

## When Is Sieve Better?

If the range is very large, repeatedly calling `is_prime` can become slow.

Another standard approach is the Sieve of Eratosthenes:

- build all prime information up to `max(n, reverse)`
- sum the prime numbers between `start` and `end`

That approach is better when:

- the upper bound is large
- there are many queries
- we need to check prime status many times

For this problem, the sieve version is usually the more standard final answer if the upper bound is large enough.

The trial division version is still good as a first solution because it is short and easy to reason about.

## Complexity

Let:

```text
R = abs(n - reverse(n)) + 1
M = max(n, reverse(n))
```

For the trial division solution:

- Time: `O(R * sqrt(M))`
- Space: `O(1)`

For the sieve solution:

- Time: `O(M log log M)`
- Space: `O(M)`
