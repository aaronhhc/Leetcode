class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        #edge case
        if p_len > s_len:
            return []

        res = []
        #frequency count for characters in p and the current window in s
        p_count = [0] * 26
        window_count = [0] * 26
        #first window
        for i in range(p_len):
            p_count[ord(p[i]) - ord('a')] += 1
            window_count[ord(s[i]) - ord('a')] += 1

        if window_count == p_count:
            res.append(0)

        #rest of the windows
        for right in range(p_len, s_len): #point
            left = right - p_len
            window_count[ord(s[right]) - ord('a')] += 1
            window_count[ord(s[left]) - ord('a')] -= 1
            if window_count == p_count:
                res.append(left + 1)

        return res

#My origin work, not as good as the above solution
class Solution:
    def isAnagram(self, s: str, sorted_p: str, start: int, p_len: int) -> bool:
        sorted_s_cur = sorted(s[start:start + p_len])
        return sorted_s_cur == sorted_p
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_len = len(p) 
        sorted_p = sorted(p)
        for start in range(len(s)):
            if s[start] not in p:
                continue
            if self.isAnagram(s, sorted_p, start, p_len) == True:
                res.append(start)
        return res
'''
this solution will TLE because of the sorting in isAnagram, which is O(nlogn) and we are doing it for every start index. The first solution uses a frequency count which is O(n) for each window and compares two lists which is O(26) = O(1), so overall it is O(n).
'''