class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        dp = costs[0][:]

        for i in range(1,n):
            curr = dp[:]
            for j in range(3):
                if j == 0:
                    curr[j] = costs[i][j] + min(dp[1:]) 
                elif j == 1:
                    curr[j] = costs[i][j] + min(dp[0], dp[2]) 
                else:
                    curr[j] = costs[i][j] + min(dp[:-1]) 
            dp = curr[:]

        return min(dp)