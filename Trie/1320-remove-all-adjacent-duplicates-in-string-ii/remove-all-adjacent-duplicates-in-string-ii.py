class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []


        for c in s:
            if not stk or stk[-1][0] != c:
                stk.append([c,1])
            else:
                stk[-1][1]+=1
                if stk[-1][1] == k:
                    stk.pop()
        
        out = ''
        while stk:
            c, count = stk.pop() 
            out = c*count + out
        
        return out
                