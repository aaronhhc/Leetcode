class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0
        left = 0
        min_len = float("inf")
        res = ""

        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        return res

'''
1. need 記 t 的需求
2. window 記目前視窗
3. right 一直擴張
4. 某字元剛好滿足需求 -> formed += 1
5. formed == required 時開始縮 left
6. 若移掉左字元後需求不滿足 -> formed -= 1
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        have = 0
        need_count = len(need)
        res = [-1, -1]
        res_len = float("inf")
        left = 0

        for right, ch in enumerate(s):
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""