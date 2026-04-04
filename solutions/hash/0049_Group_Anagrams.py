#self write solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 0:
            return [[""]]
        elif n == 1:
            return [[strs[0]]]
        
        sorted_str = []
        for string in strs:
            sorted_str.append("".join(sorted(string)))
        
        selected = [0] * n
        ans = []
        for i in range(n):
            if selected[i] == 0: 
                selected[i] = 1
                temp_list = []
                temp_list.append(strs[i])
                pivot = sorted_str[i]  
                for j in range(i + 1, n):
                    if sorted_str[j] == pivot:
                        selected[j] = 1
                        temp_list.append(strs[j])
                ans.append(temp_list)

        return ans
################################################################################
#standard solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) //ans[key].append(s)這行才不會報錯 

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)

        return list(ans.values())