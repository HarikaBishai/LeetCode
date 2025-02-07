class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
       
        stk = []
        balance = 0
        indexes_to_remove = []
        for i,c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stk.append(i)
                balance +=1
            elif c == ')':
                if balance == 0:
                    indexes_to_remove.append(i)
                else:
                    balance-=1
                    stk.pop()
            
        print(stk)
        indexes_to_remove += stk

        indexes_to_remove = set(indexes_to_remove)

        out = ''
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                out+=c
        return out
        
        

        
