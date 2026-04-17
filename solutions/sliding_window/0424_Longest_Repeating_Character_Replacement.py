class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        count = defaultdict(int)
        max_freq = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])
            window = right - left + 1
            while window - max_freq > k:
                count[s[left]] -= 1 
                left += 1
                window = right - left + 1
            res = max(res, window)
        return res
