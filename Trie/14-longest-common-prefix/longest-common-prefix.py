class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        minLen = float('inf')

        for s in strs:
            if len(s) < minLen:
                minLen = len(s)
        
        
        maxMatch = ""
        for i in range(minLen):
            curr_s = strs[0][:i+1]
            j = 1
            while j < len(strs):
                if curr_s != strs[j][:i+1]:
                    break
                j+=1
            if j == len(strs):
                maxMatch = curr_s
        return maxMatch
