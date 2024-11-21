class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for s in tokens:
            if s == '+':
                a = stk.pop()
                b = stk.pop()
                stk.append(a+b)
            elif s == '-':
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
            elif s == '*':
                a = stk.pop()
                b = stk.pop()
                stk.append(a*b)
            elif s == '/':
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b/a))
            else:
                stk.append(int(s))
        
        return stk[0]