class Solution:
    def reverse(self, x: int) -> int:
        sign = True
        if x < 0: sign = False

        x = abs(x)

        rev = 0
        div = 10
        while x:
            rem = x % div
            rev = rev * div + rem
            x = x // 10
                    
        if not sign:
            rev = -rev
        return  rev if -2 ** 31 <= rev <= (2** 31 )-1 else 0