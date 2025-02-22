class Solution:
    def calculate(self, s: str) -> int:
        out = 0
        num = 0

        stk = []
        sign = 1

        for c in s:

            if c.isdigit():
                num = num*10 + int(c)

            elif c in '+-':
                out += sign * num
                sign = 1 if c == '+' else -1
                num = 0
            elif c in '(':
                stk.append(out)
                stk.append(sign)
                out = 0
                sign = 1
            elif c == ')':
                out += num * sign
                out *= stk.pop()
                out += stk.pop()
                num = 0
                sign = 1
        return out + (num * sign )
