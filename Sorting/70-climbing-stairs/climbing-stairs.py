class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev = 1
        for i in range(2, n+1):
            curr =  prev +  prev2
            prev2 = prev
            prev = curr 
        return prev
        