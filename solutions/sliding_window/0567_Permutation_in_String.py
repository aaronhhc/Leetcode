from collections import defaultdict


#matches solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(s1_len):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        #初始化matches
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        for right in range(s1_len, s2_len):
            if matches == 26:
                return True
            add_idx = ord(s2[right]) - ord('a') 
            if s1_count[add_idx] == s2_count[add_idx]:
                matches -= 1
            s2_count[add_idx] += 1
            if s1_count[add_idx] == s2_count[add_idx]:
                matches += 1
            del_idx = ord(s2[right - s1_len]) - ord('a')
            if s1_count[del_idx] == s2_count[del_idx]:
                matches -= 1
            s2_count[del_idx] -= 1
            if s1_count[del_idx] == s2_count[del_idx]:
                matches += 1
        return matches == 26

#defaultdict solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        for ch in s1:
            s1_count[ch] += 1

        for i in range(s1_len):
            s2_count[s2[i]] += 1

        if s1_count == s2_count:
            return True

        for i in range(s1_len, s2_len):
            s2_count[s2[i]] += 1

            left_char = s2[i - s1_len]
            s2_count[left_char] -= 1
            if s2_count[left_char] == 0:
                del s2_count[left_char]

            if s1_count == s2_count:
                return True

        return False
            


            
