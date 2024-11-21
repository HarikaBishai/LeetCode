class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        openSet = set(['(', '{', '['])

        mapper = {
            '}' : '{',
            ']' : '[',
            ')' : '(' 
        }
        for i in s:
            if i in openSet:
                stk.append(i)
            else:
                if not stk:
                    return False
                top = stk.pop()
                if mapper[i] != top:
                    return False
        return False if stk else True