# 0567 Permutation in String

## Problem Idea

We are given two strings:

- `s1`
- `s2`

We need to check whether some substring of `s2` is a permutation of `s1`.

That means:

- the substring must have the same length as `s1`
- the substring must contain exactly the same character counts

Example:

- `s1 = "ab"`
- `s2 = "eidbaooo"`
- substring `"ba"` is a permutation of `"ab"`
- answer = `True`

---

## My Code Notes

This problem uses a fixed-size sliding window.

We keep a window in `s2` whose length is always:

- `len(s1)`

Then we compare the character counts of:

- `s1`
- the current window in `s2`

If the counts match, then the current window is a permutation of `s1`.

Your solution shows two common approaches:

- array counting for 26 lowercase letters
- `defaultdict` counting

Both use the same sliding-window idea.

---

## Why Sliding Window Works

Any valid permutation must:

- use exactly the same number of characters as `s1`

So we never need to check windows of different sizes.

For each window of length `len(s1)` in `s2`:

- add the new right character
- remove the old left character
- compare counts

If the counts are the same, return `True`.

If we finish scanning all windows and never match, return `False`.

---

## Array Count Idea

When the string only contains lowercase English letters, we can use:

- `26` slots for `s1`
- `26` slots for the current window in `s2`

Each index represents one character:

- `0` for `'a'`
- `1` for `'b'`
- ...
- `25` for `'z'`

This makes updates fast and predictable.

Your first solution also tracks:

- `matches`

This counts how many of the 26 character frequencies are currently equal.

If:

- `matches == 26`

then all counts match, so the window is a valid permutation.

---

## Small Example

For:

- `s1 = "ab"`
- `s2 = "eidbaooo"`

Window size is `2`.

Check windows in `s2`:

- `"ei"` -> not a match
- `"id"` -> not a match
- `"db"` -> not a match
- `"ba"` -> counts match `s1`

So we return `True`.

---

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Why:

- each character enters and leaves the window at most once
- the array size is fixed at `26`

For the hashmap version, space is still small, but more generally it is `O(m)` where `m` is the number of distinct characters.

---

## Key Learning

- This is a fixed-length sliding window problem.
- A permutation check becomes a frequency-count comparison.
- Because the window size never changes, we only update one added character and one removed character each step.
- When the alphabet is small, array counting is very efficient.
