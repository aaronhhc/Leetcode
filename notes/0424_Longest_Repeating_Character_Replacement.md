# 0424 Longest Repeating Character Replacement

## Problem Idea

We are given a string `s` and an integer `k`.

We can change at most `k` characters in the string.

The goal is to find the length of the longest substring that can become all the same character after at most `k` replacements.

Example:

- `s = "ABAB"`
- `k = 2`
- we can replace two characters to make the whole substring the same
- answer = `4`

---

## My Code Notes

This problem uses a sliding window.

We keep:

- `left`: the start of the current window
- `right`: the end of the current window, for loop is important
- `count`: how many times each character appears in the current window, and it is a dictionary
- `max_freq`: the highest frequency of any one character in the current window
- `res`: the best valid window length

Core idea:

- if the window size minus the most frequent character count is greater than `k`
- then we need more than `k` replacements
- so the window is invalid and we must move `left`

In other words:

- required replacements = `window_size - max_freq`

If that value is small enough, the window is valid.

---

## Why This Works

Inside the current window:

- one character is already the most common
- all other characters can be replaced to match it

So if:

- `window_size - max_freq <= k`

then we can convert the whole window into one repeated character.

If:

- `window_size - max_freq > k`

then we need too many replacements, so we shrink the window from the left.

This is the key sliding-window condition.

---

## Why We Keep `max_freq`

`max_freq` tells us the count of the most common character seen in the window.

That means:

- we do not need to guess which character to convert into
- we always keep the one that already appears the most

Then the only question is:

- how many other characters must be replaced

That is why the formula is:

- `window_size - max_freq`

This avoids checking all characters every time.

---

## Small Example

For:

- `s = "AABABBA"`
- `k = 1`

Consider the window `"AABA"`:

- counts: `A = 3`, `B = 1`
- `window_size = 4`
- `max_freq = 3`
- replacements needed = `4 - 3 = 1`

This is valid because `1 <= k`.

If the window becomes too large and needs more than one replacement, move `left` forward until it becomes valid again.

The longest valid answer is `4`.

---

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Why:

- each character is added to the window once
- each character is removed from the window at most once
- the character set is limited to uppercase English letters

If we describe it more generally, the space is `O(m)` where `m` is the number of distinct characters.

---

## Key Learning

- This is a classic sliding window with frequency counting.
- The important formula is `window_size - max_freq`.
- That value represents how many replacements are needed.
- If replacements needed is bigger than `k`, shrink the window.
- Tracking the most frequent character lets us solve the problem in linear time.
