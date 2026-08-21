# 0274 H-Index

## Problem

Given an array `citations`, where `citations[i]` is the number of citations for
paper `i`, return the researcher's H-Index.

The H-Index is the largest value `h` such that the researcher has published at
least `h` papers, and each of those papers has at least `h` citations.

Example:

```text
citations = [3, 0, 6, 1, 5]
```

Result:

```text
3
```

There are three papers with at least three citations: `3`, `6`, and `5`.
There are not four papers with at least four citations, so the H-Index is `3`.

---

## My Code Notes

The solution uses bucket counting, also called frequency counting.

Instead of sorting every citation count, create a bucket for each possible H-Index
value and count how many papers belong to each bucket.

```python
n = len(citations)
count = [0] * (n + 1)

for c in citations:
    count[min(c, n)] += 1

paper = 0

for h in range(n, -1, -1):
    paper += count[h]
    if paper >= h:
        return h
```

---

## What Does H-Index Mean?

For a candidate value `h`, two conditions must be true:

- at least `h` papers have been published
- each of those papers has at least `h` citations

Equivalently, we can count how many papers have citation counts greater than or
equal to `h`. If that number is at least `h`, then `h` is a valid H-Index.

We want the largest valid `h`.

---

## Why Can the H-Index Be At Most `n`?

Let `n` be the total number of papers.

The H-Index cannot be larger than `n` because the researcher cannot have more
than `n` papers with at least `h` citations. Therefore, even if every paper has
many citations, the maximum possible H-Index is still `n`.

This is why the code starts with:

```python
n = len(citations)
```

and only needs to consider candidate values from `n` down to `0`.

---

## Bucket Counting

Create `n + 1` buckets:

```python
count = [0] * (n + 1)
```

The indexes represent citation counts from `0` through `n`.

The extra bucket at index `n` is important. It represents:

- exactly `n` citations
- every citation count greater than `n`

For example, if `n = 5`, the buckets represent:

```text
count[0], count[1], count[2], count[3], count[4], count[5]
```

Here, `count[5]` means the number of papers with at least `5` citations, not
only the number with exactly `5` citations.

---

## Why Use `count[min(c, n)]`?

The code places each citation count into a bucket:

```python
for c in citations:
    count[min(c, n)] += 1
```

If `c < n`, the paper goes into its exact citation bucket.

If `c >= n`, `min(c, n)` equals `n`, so the paper goes into `count[n]`.

All values greater than `n` can be combined because the H-Index can never be
larger than `n`. For deciding whether a candidate `h <= n` is valid, a paper
with `n` citations and a paper with `100` citations both satisfy the requirement
of having at least `h` citations.

This also prevents the code from creating an unnecessarily large bucket array
when a citation count is very large.

---

## Why Scan from `n` Down to `0`?

The goal is to find the largest valid H-Index, so test the largest possible
candidate first:

```python
for h in range(n, -1, -1):
```

The first `h` that satisfies the H-Index condition must be the answer. There is
no need to continue checking smaller values after finding it.

---

## What Does `paper` Represent?

`paper` is the number of papers whose citation count is at least the current
candidate `h`.

The loop accumulates buckets from high citation counts toward lower citation
counts:

```python
paper += count[h]
```

At the moment we are checking `h`, `paper` contains:

```text
count[h] + count[h + 1] + ... + count[n]
```

Therefore, it represents the number of papers with citations `>= h`.

For example, when checking `h = 3`, the accumulated buckets include papers in
buckets `3`, `4`, and `5`, so all counted papers have at least `3` citations.

---

## Why Return `h` Instead of `paper`?

The H-Index is the candidate threshold `h`, not the number of qualifying papers
`paper`.

The condition is:

```python
if paper >= h:
    return h
```

Here:

- `paper` answers: how many papers have at least `h` citations?
- `h` answers: what H-Index candidate are we testing?

The number of qualifying papers may be larger than `h`. For example, if `h = 3`
and `paper = 5`, the H-Index candidate being verified is still `3`.

Because the loop checks candidates from largest to smallest, returning this
first valid `h` gives the maximum H-Index.

---

## Complete Walkthrough

Use:

```text
citations = [3, 0, 6, 1, 5]
n = 5
```

After creating the buckets and applying `count[min(c, n)] += 1`:

```text
count[0] = 1   # citation 0
count[1] = 1   # citation 1
count[2] = 0
count[3] = 1   # citation 3
count[4] = 0
count[5] = 2   # citations 5 and 6; 6 is grouped into bucket 5
```

Now scan from `h = 5` down to `0`:

| `h` | `paper` after `paper += count[h]` | Check | Result |
|---:|---:|---|---|
| 5 | 2 | `2 >= 5` is false | continue |
| 4 | 2 | `2 >= 4` is false | continue |
| 3 | 3 | `3 >= 3` is true | return `3` |

The answer is `3`.

Notice that when `h = 3`, the three qualifying papers are the papers with
citations `3`, `5`, and `6`.

---

## Sorting Solution

A more direct approach is to sort the citations first:

```python
sorted_citations = sorted(citations)
n = len(citations)

for i in range(n):
    if sorted_citations[i] >= n - i:
        return n - i

return 0
```

After sorting, for a paper at index `i`, there are `n - i` papers from index `i`
to the end. If `sorted_citations[i] >= n - i`, then those `n - i` papers each
have at least `n - i` citations, so `n - i` is a valid H-Index candidate.

Because the array is sorted, the first valid candidate found while scanning from
left to right is the largest valid candidate.

The sorting solution is often easier to understand, while the bucket solution
avoids sorting and runs in linear time.

---

## Bucket Counting vs Sorting

| Approach | Time | Extra Space | Main idea |
|---|---:|---:|---|
| Sorting | `O(n log n)` | `O(n)` for Python's sorted result | Sort citation counts and inspect suffix lengths |
| Bucket counting | `O(n)` | `O(n)` | Count citation frequencies and accumulate from high to low |

Bucket counting is useful here because the answer is bounded by the number of
papers, `n`. Citation counts much larger than `n` do not need separate buckets.

---

## Common Confusions

- `n` is the number of papers, not the largest citation count.
- The H-Index is limited by the number of papers, even when citation counts are
  extremely large.
- `count[n]` includes every paper with `n` or more citations.
- `paper` is a running count of papers with citations at least `h`.
- `paper >= h` checks whether the current candidate is valid; it does not mean
  that `paper` is the answer.
- The function returns `h` because the H-Index is the threshold being tested.
- Scanning from high to low allows the function to return immediately at the
  first valid candidate.
- The loop includes `h = 0`. An H-Index of `0` is valid when no positive
  candidate can satisfy the condition.

---

## Complexity

- Time: `O(n)`
- Space: `O(n)`

The bucket array has `n + 1` entries. Each citation is processed once, and the
final scan checks at most `n + 1` buckets.

The alternative sorting solution takes `O(n log n)` time because of sorting.
