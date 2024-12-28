class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out = 0
        stk = []
        for t in tokens:
            if t == '+':
                a = stk.pop()
                b = stk.pop()
                stk.append(b+a)
            elif t == '-':
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
            elif t == '/':
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b/a))
            elif t == '*':
                a = stk.pop()
                b = stk.pop()
                stk.append(b*a)
            else:
                stk.append(int(t))
        return stk[0]