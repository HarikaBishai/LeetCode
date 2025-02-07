class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
       
        stk = []
        indexes_to_remove = []
        for i,c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stk.append(i)
            elif c == ')':
                if len(stk) == 0:
                    indexes_to_remove.append(i)
                else:
                    stk.pop()
            
        indexes_to_remove += stk

        indexes_to_remove = set(indexes_to_remove)

        out = ''
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                out+=c
        return out
        
        

        
