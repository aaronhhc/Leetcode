#self write solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = set(nums)
        freq = dict.fromkeys(keys, 0)
        for num in nums:
            freq[num] += 1
        sorted_freq = dict(sorted(freq.items(), key = lambda x:x[1], reverse = True))
        return list(sorted_freq.keys())[:k]

#better solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        sorted_freq = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        return [num for num, count in sorted_freq[:k]]

#bucket solution (frequency <= n so we can use bucket sort)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
        
        ans = []
        for count in range(len(bucket) - 1, 0, -1):
            for num in bucket[count]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        

        