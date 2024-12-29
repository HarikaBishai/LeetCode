class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stk = []

        for char in s:
            if not stk:
                stk.append((1,char))
            else:
                count = 1
                while stk and stk[-1][1] == char:
                    count +=  stk.pop()[0]
                
                if count == k:
                    continue
                else:
                    stk.append((count, char))
        out = ''

        while stk:
            count, char = stk.pop()
            out = count*char + out 
        return out