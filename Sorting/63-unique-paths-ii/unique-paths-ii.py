class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 :
            return 0
        dp = [[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                up = 0
                if i>0 and obstacleGrid[i-1][j]!=1:
                    up = dp[i-1][j]
                left = 0
                if j > 0 and obstacleGrid[i][j-1]!=1:
                    left = dp[i][j-1]
                
                dp[i][j] = up + left
        return dp[m-1][n-1]