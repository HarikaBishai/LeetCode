class Solution:
    def calculate(self, s: str) -> int:
        
        out = 0
        curr = 0
        sign  = 1
        stk = []
        for c in s:
            print(out)
            if c.isdigit():
                curr = curr*10 + int(c)
            elif c in '+-':
                out += curr*sign
                curr = 0
                if c == '+':
                    sign = 1
                else:
                    sign = -1
            elif c == '(':
                stk.append(out)
                stk.append(sign)
                out = 0
                sign = 1
            elif c == ')':
                out += curr*sign
                out *= stk.pop()
                out += stk.pop()
                curr = 0
        print(stk)
        return out + (curr * sign)
