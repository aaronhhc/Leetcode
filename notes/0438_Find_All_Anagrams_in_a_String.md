# 0438 Find All Anagrams in a String

## Problem Idea

We are given two strings:

- `s`
- `p`

We need to find every starting index in `s` where the substring is an anagram of `p`.

That means:

- the substring length must be exactly `len(p)`
- the substring must contain the same character counts as `p`

Example:

- `s = "cbaebabacd"`
- `p = "abc"`
- valid substrings are `"cba"` and `"bac"`
- answer = `[0, 6]`

---

## My Code Notes

This problem is a fixed-size sliding window.

Your code keeps:

- `p_count`: frequency count of characters in `p`
- `window_count`: frequency count of the current window in `s`
- `res`: all starting indices whose window matches `p`

The window size is always:

- `len(p)`

So the work for each step is:

- add the new right character
- remove the old left character
- compare the two frequency arrays

If the arrays are equal, that window is an anagram.

---

## Why Sliding Window Works

An anagram of `p` must use:

- the same letters
- the same counts
- the same total length

Because of that, we never need to check substrings longer or shorter than `p`.

We only scan all windows of size `len(p)` inside `s`.

This makes the solution efficient because each move only changes:

- one entering character
- one leaving character

---

## Array Count Idea

Since the problem uses lowercase English letters, we can use an array of size `26`.

Index mapping:

- `0` -> `'a'`
- `1` -> `'b'`
- ...
- `25` -> `'z'`

This line does the mapping:

```python
ord(char) - ord('a')
```

Why this is nice:

- updates are `O(1)`
- space is fixed
- array comparison is simple

---

## How Your Code Flows

### 1. Edge case

If `p` is longer than `s`, no answer is possible:

```python
if p_len > s_len:
    return []
```

### 2. Build the first window

You count:

- every character in `p`
- the first `p_len` characters in `s`

Then you compare them once.

If they match, index `0` is valid.

### 3. Slide the window

For every next position:

- add `s[right]`
- remove `s[left]`
- compare `window_count` with `p_count`

If they match, append `left + 1`, which is the new start index.

---

## Small Example

For:

- `s = "abab"`
- `p = "ab"`

Window size is `2`.

Check each window:

- `"ab"` -> match, add `0`
- `"ba"` -> match, add `1`
- `"ab"` -> match, add `2`

Answer:

- `[0, 1, 2]`

---

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Why:

- each window move updates only two characters
- the count arrays always have size `26`
- comparing two size-26 arrays is constant time

More precisely, the runtime is:

- `O(len(s) * 26)`

which is still linear because `26` is constant.

---

## Key Learning

- This is a classic fixed-length sliding window problem.
- Anagram checking becomes frequency-array comparison.
- When the alphabet is small, array counting is faster and cleaner than a hashmap.
- The important trick is to update the window instead of rebuilding counts from scratch.
