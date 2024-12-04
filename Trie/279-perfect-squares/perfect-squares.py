class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = i
            for j in range(1,int(i**0.5)+1):

                dp[i] = min(dp[i],1+ dp[i-j*j])
        
        return dp[n]