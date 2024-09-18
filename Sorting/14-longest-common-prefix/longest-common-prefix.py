class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s_l = min(strs, key=len)
        out = ''
        cnt = 0
        for i in range(len(s_l)):
            c = strs[0][i]
            j = 1
            while j < len(strs):
                if strs[j][i] != c:
                    break
                j+=1
            if j == len(strs):
                cnt+=1
            else:
                break
        return strs[0][0:cnt]
                
