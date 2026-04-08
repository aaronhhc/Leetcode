# 0125 Valid Palindrome

## Problem Idea

We need to decide whether a string is a palindrome after:

- converting uppercase letters to lowercase
- removing all non-alphanumeric characters

That means spaces, commas, colons, and other symbols should be ignored.

Example:

- `s = "A man, a plan, a canal: Panama"`
- cleaned string becomes `"amanaplanacanalpanama"`
- this reads the same forward and backward
- answer: `True`

Another example:

- `s = "race a car"`
- cleaned string becomes `"raceacar"`
- this is not the same forward and backward
- answer: `False`

---

## My Code Notes

### 1. Self-written two-pointer solution

```python
s = "".join(char.lower() for char in s if char.isalnum())
left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1

return True
```

What this version does:

- `char.isalnum()` keeps only letters and digits.
- `char.lower()` converts letters to lowercase.
- `"".join(...)` builds the cleaned string first.
- Then two pointers compare characters from both ends.

Why two pointers work:

- In a palindrome, the first and last characters must match.
- Then the second and second-last must match.
- We keep moving inward until the pointers meet.

If any pair is different, the string is not a palindrome.

---

### 2. One-liner solution

```python
s = "".join(char.lower() for char in s if char.isalnum())
return s == s[::-1]
```

Main idea:

- Clean the string in the same way.
- `s[::-1]` creates the reversed string.
- Compare the cleaned string with its reverse.

This is shorter and very Pythonic.

---

## Key Python Concepts

### `isalnum()`

Checks whether a character is a letter or a digit.

Examples:

- `'a'.isalnum()` -> `True`
- `'7'.isalnum()` -> `True`
- `' '.isalnum()` -> `False`
- `','.isalnum()` -> `False`

This is why punctuation and spaces are removed.

---

### `lower()`

Converts uppercase letters to lowercase.

Examples:

- `'A'.lower()` -> `'a'`
- `'P'.lower()` -> `'p'`

This makes the comparison case-insensitive.

---

### String slicing: `[::-1]`

Reverses a string.

Example:

```python
"abc"[::-1]   # "cba"
```

So:

```python
s == s[::-1]
```

means:

- compare the string with its reversed version

---

## Complexity

For both versions:

- Time: `O(n)`
- Space: `O(n)`

Why:

- We scan the string once to build the cleaned version.
- The two-pointer check is `O(n)`.
- The reverse comparison is also `O(n)`.
- We store a new cleaned string, so extra space is needed.

---

## Key Learning

- Always read the problem carefully: we are not checking the original string directly.
- Preprocessing the string first makes the palindrome check much easier.
- Two pointers are a common pattern for palindrome problems.
- Python slicing can make the solution shorter, but the two-pointer version is good practice.
