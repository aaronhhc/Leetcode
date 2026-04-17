#my code
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        left, right = 0, 1
        res = 0
        lgs = [s[left]]
        while right < n :
            if s[right] not in lgs:
                lgs.append(s[right])
                right += 1
            else:
                res = max(res, len(lgs))
                lgs.clear()
                left += 1
                right = left + 1
                lgs.append(s[left])
        return max(res, len(lgs))
#standard code
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        lgs = set()
        res = 0
        for right in range(len(s)):
            while s[right] in lgs:
                lgs.remove(s[left])
                left += 1
            lgs.add(s[right])
            res = max(res, right - left + 1)
        return res