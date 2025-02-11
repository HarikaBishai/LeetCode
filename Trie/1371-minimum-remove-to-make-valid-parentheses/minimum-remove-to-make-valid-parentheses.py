class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stk = []
        index_to_remove = []

        for i,c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stk.append(i)
            else:
                if stk:
                    stk.pop()
                else:
                    index_to_remove.append(i)

        index_to_remove = set(index_to_remove + stk)

        out = ''

        for i, c in enumerate(s):
            if i not in index_to_remove:
                out+=c
        return out