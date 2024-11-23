class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if k == 1: return ""
        stk = []

        for char in s:
            count = 1
            if stk and stk[-1][0] == char:
                topChar, topCount = stk.pop()
                count+=topCount
            
            if count == k:
                continue
            else:
                stk.append((char,count))
        
        out = ""

        for char,count in stk:
            out+=char*count
        
        return out
        

            