# 0076 Minimum Window Substring

## Problem Idea

We are given two strings:

- `s`
- `t`

We need to find the smallest substring in `s` that contains all characters in `t`.

Important:

- the characters must appear with the correct frequency
- order does not matter

Example:

- `s = "ADOBECODEBANC"`
- `t = "ABC"`
- the answer is `"BANC"`

---

## My Code Notes

This problem uses a variable-size sliding window.

We keep:

- `need`: how many times each character is required from `t`
- `window`: how many times each character appears in the current window
- `left`: the left boundary of the window
- `right`: the right boundary of the window
- `have`: how many character types currently satisfy the required count
- `need_count`: how many distinct character types must be satisfied

Core idea:

- move `right` to expand the window until it becomes valid
- once the window contains all required characters, move `left` to shrink it
- keep updating the shortest valid window

So the pattern is:

- expand until valid
- shrink until invalid
- repeat

---

## Why Sliding Window Works

We do not need to check every substring from scratch.

Instead:

- when `right` moves, we add one character into the window
- when `left` moves, we remove one character from the window

This lets us maintain the character counts efficiently.

The window is valid when:

- every character in `t` appears enough times in the current window

In the code, that means:

- `have == need_count`

When the window is valid:

- update the answer if this window is smaller
- try shrinking from the left to make it as short as possible

When removing the left character makes some count fall below what `t` needs:

- the window becomes invalid
- stop shrinking
- continue expanding with `right`

---

## Why `have` and `need_count` Matter

We do not compare the whole hashmap every time.

Instead:

- `need_count` is the number of distinct characters in `t`
- `have` counts how many of those characters are currently satisfied

For example, if:

- `t = "AABC"`

then:

- `need["A"] = 2`
- `need["B"] = 1`
- `need["C"] = 1`
- `need_count = 3`

Even though `t` has length `4`, we only need to track whether the required count for each distinct character is satisfied.

This makes checking validity much faster.

---

## Small Example

For:

- `s = "ADOBECODEBANC"`
- `t = "ABC"`

At first, expand `right` until the window contains:

- `A`
- `B`
- `C`

Now the window is valid.

Then move `left` forward to remove unnecessary characters.

We keep repeating this:

- find a valid window
- shrink it as much as possible
- store the shortest one

Eventually, the minimum valid window becomes:

- `"BANC"`

---

## Complexity

- Time: `O(|s| + |t|)`
- Space: `O(|s| + |t|)` in the hashmap implementation

Why:

- building `need` takes `O(|t|)`
- each character in `s` enters the window once
- each character in `s` leaves the window at most once

So both pointers move forward only once overall.

---

## Key Learning

- This is a classic variable-length sliding window problem.
- Use frequency maps to track what is needed and what is currently inside the window.
- The window becomes valid when all required character counts are satisfied.
- Once valid, shrink from the left to get the minimum window.
- The expand-then-shrink pattern is the key idea for minimum-window problems.
