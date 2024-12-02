class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        dp = [[0] * 3 for _ in range(n)]

        dp[0] = costs[0][:]
        for i in range(1,n):
            for j in range(3):
                if j == 0:
                    dp[i][j] = costs[i][j] + min(dp[i-1][1:]) 
                elif j == 1:
                    dp[i][j] = costs[i][j] + min(dp[i-1][0], dp[i-1][2]) 
                else:
                    dp[i][j] = costs[i][j] + min(dp[i-1][:-1]) 

        print(dp)     
        return min(dp[n-1])