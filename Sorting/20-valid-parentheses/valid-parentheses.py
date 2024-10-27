class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for r in s:
            if r in ['(','[','{']:
                stk.append(r)
            else:
                if not stk:
                    return False
                elif (stk[-1] == '(' and r == ')' )or (stk[-1] == '[' and r == ']' )or (stk[-1] == '{' and r == '}'):
                    stk.pop()
                else:
                    return False
                
        if stk:
            return False
        return True
