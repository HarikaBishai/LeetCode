class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1 
        r = (x+1)//2

        res = 0

        while l <= r:
            mid = (l+r)//2
            squareVal = mid*mid
            if squareVal == x:
                return mid
            if squareVal > x:
                r = mid-1
            else:
                l+=1
                res = max(res, mid)
        return res