class Solution:
    def myAtoi(self, s: str) -> int:
        

        s = s.lstrip(" ")

        if not s:
            return 0
        
        sign = True
        if s[0] in '+-':
            if s[0] == '-':
                sign = False
            s = s[1:]
        num = 0

        for c in s:
            if not c.isdigit():
                break
            num = num*10 + int(c)
        
        left_boundary = -pow(2, 31)
        right_boundary = pow(2,31)-1

        num = -num if not sign else num

        if num < left_boundary:
            return left_boundary
        elif num > right_boundary:
            return right_boundary
        else:
            return num