# LeetCode 33 Search in Rotated Sorted Array 筆記

## 1. 題目本質

This problem is a variation of binary search.

In normal binary search, the whole array is sorted.

But in this problem, the array was sorted first, then rotated.

Example:

```text
Original sorted array:
[0, 1, 2, 4, 5, 6, 7]

After rotation:
[4, 5, 6, 7, 0, 1, 2]
```

So the array is not fully sorted anymore.

But it still has structure:

- one part is sorted
- another part is also sorted
- there is only one break point

The goal is still to remove half of the search range each time.

The new problem is: we cannot blindly compare `nums[mid]` and `target` anymore.

---

## 2. 傳統 Binary Search vs Rotated Binary Search

| Topic | Traditional Binary Search | Rotated Binary Search |
|---|---|---|
| Array shape | Fully sorted | Sorted, then rotated |
| Can compare `nums[mid]` with `target` directly? | Yes | Not enough |
| Main question | Is target smaller or larger than `nums[mid]`? | Which half is sorted? |
| Direction rule | `nums[mid] < target` means go right | First find the sorted half, then check if target is inside it |
| Why it works | Every left value is smaller, every right value is larger | At least one half is still sorted |

---

## 3. 核心觀念

The important ideas are:

- A rotated sorted array has only one break point.
- Every time we cut the range into two halves, at least one half must be sorted.
- Only the sorted half can be checked with a clean range condition.

For example:

```text
nums = [4, 5, 6, 7, 0, 1, 2]
```

If we choose:

```text
left = 0
mid = 3
right = 6
```

Then:

```text
left half  = [4, 5, 6, 7]  sorted
right half = [0, 1, 2]     sorted
```

Sometimes both halves look sorted.

But the key promise is simpler:

```text
At least one half is sorted.
```

So the safe strategy is:

1. Find the sorted half.
2. Ask if `target` belongs inside that sorted half.
3. If yes, search there.
4. If no, search the other half.

---

## 4. 為什麼不能直接看 target 在哪邊？

In normal binary search, this works:

```python
if nums[mid] < target:
    left = mid + 1
else:
    right = mid - 1
```

Because the whole array is sorted.

If `nums[mid] < target`, everything on the left side is also smaller than `target`, so we can ignore the left side.

But in a rotated array, the left and right sides are not guaranteed to follow that rule.

Counterexample:

```text
nums = [6, 7, 0, 1, 2, 4, 5]
target = 0
```

Start:

```text
left = 0
right = 6
mid = 3

nums[left] = 6
nums[mid] = 1
nums[right] = 5
```

If we directly write:

```python
if nums[left] <= target < nums[mid]:
    right = mid - 1
else:
    left = mid + 1
```

We check:

```text
6 <= 0 < 1
```

This is false.

So this wrong logic moves right:

```text
left = mid + 1 = 4
```

But the target `0` is actually at index `2`, on the left side.

Why did it fail?

Because `[6, 7, 0, 1]` is not sorted.

The condition:

```python
nums[left] <= target < nums[mid]
```

only makes sense when the left half is sorted.

That is why we must first ask:

```text
Is the left half sorted?
```

Do not check whether `target` is in a half before knowing that half is sorted.

---

## 5. 正確判斷流程

At each loop:

1. Check if `nums[mid]` is the target.
2. Check whether the left half is sorted.
3. If the left half is sorted, check whether `target` is inside the left half.
4. If the left half is not sorted, the right half must be sorted.
5. Check whether `target` is inside the right half.

The core condition for left half sorted:

```python
nums[left] <= nums[mid]
```

Why `<=`?

Because when `left == mid`, the left half has only one value.

A one-value array is still sorted.

Example:

```text
nums = [3, 1]
left = 0
right = 1
mid = 0
```

Here:

```text
left == mid
nums[left] == nums[mid]
```

So we need:

```python
nums[left] <= nums[mid]
```

If we use `<`, we would incorrectly say the left half is not sorted.

---

## 6. 正確程式碼

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

---

## 7. Trace 範例

### Example 1

```text
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```

Round 1:

```text
left = 0, mid = 3, right = 6
nums[left] = 4, nums[mid] = 7, nums[right] = 2
```

Check target:

```text
nums[mid] == target?
7 == 0 -> no
```

Check sorted half:

```text
nums[left] <= nums[mid]
4 <= 7 -> true
```

So the left half `[4, 5, 6, 7]` is sorted.

Check if target is inside the sorted left half:

```text
nums[left] <= target < nums[mid]
4 <= 0 < 7 -> false
```

So target is not in the sorted left half.

Search the other half:

```text
left = mid + 1 = 4
right = 6
```

Round 2:

```text
left = 4, mid = 5, right = 6
nums[left] = 0, nums[mid] = 1, nums[right] = 2
```

Check target:

```text
nums[mid] == target?
1 == 0 -> no
```

Check sorted half:

```text
nums[left] <= nums[mid]
0 <= 1 -> true
```

So the left half `[0, 1]` is sorted.

Check if target is inside:

```text
nums[left] <= target < nums[mid]
0 <= 0 < 1 -> true
```

Search the left half:

```text
right = mid - 1 = 4
```

Round 3:

```text
left = 4, mid = 4, right = 4
nums[left] = 0, nums[mid] = 0, nums[right] = 0
```

Check target:

```text
nums[mid] == target?
0 == 0 -> yes
```

Return:

```text
4
```

### Example 2

```text
nums = [6, 7, 0, 1, 2, 4, 5]
target = 0
```

Round 1:

```text
left = 0, mid = 3, right = 6
nums[left] = 6, nums[mid] = 1, nums[right] = 5
```

Check target:

```text
nums[mid] == target?
1 == 0 -> no
```

Check sorted half:

```text
nums[left] <= nums[mid]
6 <= 1 -> false
```

So the left half is not sorted.

That means the right half `[1, 2, 4, 5]` must be sorted.

Check if target is inside the sorted right half:

```text
nums[mid] < target <= nums[right]
1 < 0 <= 5 -> false
```

So target is not in the sorted right half.

Search the other half:

```text
right = mid - 1 = 2
```

Round 2:

```text
left = 0, mid = 1, right = 2
nums[left] = 6, nums[mid] = 7, nums[right] = 0
```

Check target:

```text
nums[mid] == target?
7 == 0 -> no
```

Check sorted half:

```text
nums[left] <= nums[mid]
6 <= 7 -> true
```

So the left half `[6, 7]` is sorted.

Check if target is inside:

```text
nums[left] <= target < nums[mid]
6 <= 0 < 7 -> false
```

Search the other half:

```text
left = mid + 1 = 2
```

Round 3:

```text
left = 2, mid = 2, right = 2
nums[left] = 0, nums[mid] = 0, nums[right] = 0
```

Check target:

```text
nums[mid] == target?
0 == 0 -> yes
```

Return:

```text
2
```

### Example 3: Why `<=` matters

```text
nums = [3, 1]
target = 1
```

Round 1:

```text
left = 0, mid = 0, right = 1
nums[left] = 3, nums[mid] = 3, nums[right] = 1
```

Check target:

```text
nums[mid] == target?
3 == 1 -> no
```

Now check if left half is sorted:

```text
nums[left] <= nums[mid]
3 <= 3 -> true
```

This is correct.

The left half only has one value:

```text
[3]
```

A one-value half is sorted.

Check if target is inside this sorted left half:

```text
nums[left] <= target < nums[mid]
3 <= 1 < 3 -> false
```

So target is not in the left half.

Search the other half:

```text
left = mid + 1 = 1
```

Round 2:

```text
left = 1, mid = 1, right = 1
nums[left] = 1, nums[mid] = 1, nums[right] = 1
```

Check target:

```text
nums[mid] == target?
1 == 1 -> yes
```

Return:

```text
1
```

If we used:

```python
nums[left] < nums[mid]
```

Then in Round 1:

```text
3 < 3 -> false
```

The code would think the left half is not sorted.

That is wrong because `[3]` is sorted.

This is why `<=` is important.

---

## 8. 常見錯誤

### Mistake 1: Directly using `nums[mid] < target`

This works only when the whole array is sorted.

In a rotated array:

```text
[4, 5, 6, 7, 0, 1, 2]
```

`target` may be smaller than `nums[mid]` but still on the right side.

### Mistake 2: Not checking which half is sorted first

This is the most common confusion.

Range checks like this:

```python
nums[left] <= target < nums[mid]
```

only work if `nums[left] ... nums[mid]` is sorted.

So sorted-half detection must come first.

### Mistake 3: Using `<` instead of `<=`

Use:

```python
nums[left] <= nums[mid]
```

Because when `left == mid`, the left half has one element, and one element is sorted.

### Mistake 4: Writing the boundary conditions incorrectly

For the left sorted half:

```python
nums[left] <= target < nums[mid]
```

For the right sorted half:

```python
nums[mid] < target <= nums[right]
```

Notice that `nums[mid]` is excluded because we already checked it.

### Mistake 5: Updating to `mid` instead of `mid + 1` or `mid - 1`

After checking:

```python
if nums[mid] == target:
    return mid
```

We know `mid` is not the answer.

So we should remove it:

```python
left = mid + 1
right = mid - 1
```

Using `left = mid` or `right = mid` may cause an infinite loop.

---

## 9. 一句話總結

Traditional binary search uses `nums[mid]` and `target` to decide left or right because the whole array is sorted.

Rotated binary search first asks which half is sorted, because only a sorted half can be checked by range.

The core template is: check `mid`, find the sorted half, check whether `target` belongs there, then discard the other half.
