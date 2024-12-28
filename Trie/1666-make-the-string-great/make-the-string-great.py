class Solution:
    def makeGood(self, s: str) -> str:
        stk = []

        for char in s:
            if stk:
                top = stk[-1]
                if top != char and top.lower() == char.lower():
                    stk.pop()
                else:
                    stk.append(char)
            else:
                stk.append(char)
        return "".join(stk)