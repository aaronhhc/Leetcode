# 0049 Group Anagrams

## Idea

Anagrams will have the same characters after sorting.

So for each string:

1. sort the string
2. use the sorted result as a key
3. group all strings with the same key together

## Key Insight

If two words are anagrams, their sorted forms are the same.

Example:

- `"eat"` → `"aet"`
- `"tea"` → `"aet"`
- `"ate"` → `"aet"`

So they belong to the same group.

## Why `defaultdict(list)`?

We want to group strings by key.

With `defaultdict(list)`, each new key automatically starts with an empty list,  
so we can directly write:

`ans[key].append(s)`

without checking whether the key already exists.



## Example

For `strs = ["eat","tea","tan","ate","nat","bat"]`

The grouped result is:

- `["eat", "tea", "ate"]`
- `["tan", "nat"]`
- `["bat"]`

## Complexity

- Time: `O(n * k log k)`  
  where `n` is the number of strings, and `k` is the average string length  
  because each string needs to be sorted

- Space: `O(n * k)`

## Note

The key idea is:

- sort each string
- use the sorted string as a hash key
- collect all strings with the same key into one group

## Python Dictionary Reminder

- `dict.keys()` → all keys
- `dict.values()` → all values
- `dict.items()` → all key-value pairs

In this problem, we only need the grouped lists, so we return:

`list(ans.values())`