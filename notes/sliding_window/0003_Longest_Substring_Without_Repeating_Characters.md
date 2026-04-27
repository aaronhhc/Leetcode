# 0003 Longest Substring Without Repeating Characters

## Problem Idea

We are given a string `s`.

We need to find the length of the longest substring that contains no repeated characters.

Important detail:

- A substring must be continuous.
- We only need the length, not the substring itself.

Example:

- `s = "abcabcbb"`
- the longest valid substring is `"abc"`
- answer = `3`

---

## My Code Notes

The standard solution uses a sliding window.

We keep:

- `left`: the start of the current window
- `right`: the end of the current window
- `lgs`: a set of characters currently inside the window
- `res`: the best length seen so far

Core idea:

- expand the window by moving `right`
- if the new character is repeated, shrink the window from the left
- keep shrinking until the window becomes valid again

This way, the window always contains unique characters.

---

## Why Sliding Window Works

If `s[right]` is not inside the set:

- we can safely add it
- the current window is still valid

If `s[right]` is already inside the set:

- the window now has a duplicate
- we remove `s[left]`
- move `left` forward
- repeat until the duplicate is gone

After that, the window is valid again, so we update the answer.

The key is:

- each character enters the window once
- each character leaves the window at most once

So the whole process is linear.

---

## Small Example

For:

- `s = "pwwkew"`

Step by step:

- start with `"p"` -> length `1`
- add `"w"` -> window becomes `"pw"` -> length `2`
- next character is another `"w"` -> duplicate found
- move `left` until the old `"w"` is removed
- continue expanding to get `"wke"` -> length `3`

So the answer is `3`.

---

## Complexity

- Time: `O(n)`
- Space: `O(min(n, m))`

Here:

- `n` is the length of the string
- `m` is the size of the character set

In practice, we usually just say the extra space is `O(n)`.

---

## Key Learning

- This is a classic sliding window problem.
- Use a set to quickly detect repeated characters in the current window.
- When a duplicate appears, do not restart from scratch.
- Shrink the left side only as much as needed, then keep expanding.
