class Solution:
    def reverse(self, x: int) -> int:
        sign = True

        if x < 0:
            sign = False
        
        x = abs(x)

        out = 0
        while x > 0:
            out = out * 10 + x%10
            x = x//10
        out = -out if not sign else out
        return out if -pow(2, 31) <= out <= (pow(2,31) -1 )else 0