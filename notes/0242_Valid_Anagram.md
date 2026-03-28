# 0242. Valid Anagram

## Problem
Determine whether two strings `s` and `t` are **anagrams** of each other.

An anagram means:
- Both strings contain the **same characters**
- Each character appears the **same number of times**

---

## Example

**Input**

s = "anagram"  
t = "nagaram"

**Output**

true

---

## Approach

Use **frequency counting** to compare the number of occurrences of each character.

Steps:
1. Create an array of size **26** (for `a–z`).
2. Increment counts for characters in `s`.
3. Decrement counts for characters in `t`.
4. If all counts are `0`, the strings are anagrams.

---

## Key Concepts

### `ord()`
Convert character → integer.

Example:

ord('a') = 97  
ord('b') = 98

Mapping characters to array index:

index = ord(c) - ord('a')

Result:

a → 0  
b → 1  
...  
z → 25

---

### `all()`

Check if every element satisfies a condition.

Example:

all(x == 0 for x in count)

Returns `True` only if all values are `0`.

---

## Complexity

Time Complexity: **O(n)**  
Space Complexity: **O(1)** (fixed array size 26)

---

## Python Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for c in t:
            count[ord(c) - ord('a')] -= 1

        return all(x == 0 for x in count)
