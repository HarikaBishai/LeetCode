class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def parseString(s):
            stk = []
            for i in range(len(s)):
                if s[i] != '#':
                    stk.append(s[i])
                else:
                    if stk:
                        stk.pop()
            return stk[::-1]
        
        return parseString(s) == parseString(t)
        