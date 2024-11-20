class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
            minLen = float('inf')

            for s in strs:
                if len(s) < minLen:
                    minLen = len(s)

            out = ''
            for i in range(minLen):
                c = ""
                j = 0
                while j < len(strs):
                    s = strs[j]
                    if not c:
                        c = s[i]
                    elif c!=s[i]:
                        break
                    j+=1
                if j == len(strs):
                    out+=c
                else:
                    break
            return out




