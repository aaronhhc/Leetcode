#self write solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)
        n = len(numbers)
        for i in range(n):
            com = target - numbers[i]
            if com in num_dict:
                return [min(i + 1, num_dict[com] + 1), max(i + 1, num_dict[com] + 1)]
            num_dict[numbers[i]] = i

#two pointers solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 #point to smallest
        right = len(numbers) - 1 #point to the largest
        while(left < right):
            cur_total = numbers[left] + numbers[right]
            if target > cur_total:
                left += 1
            elif target < cur_total:
                right -= 1
            else:
                return [left + 1, right + 1]