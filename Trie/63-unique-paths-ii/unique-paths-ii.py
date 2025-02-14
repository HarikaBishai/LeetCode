class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        for i in range(ROWS):
            if obstacleGrid[i][0] == 1 or( i > 0 and dp[i-1][0] ==  0 ):
                dp[i][0] = 0
            else:
                dp[i][0] = 1
        
        for i in range(COLS):
            if obstacleGrid[0][i] == 1 or (i > 0 and dp[0][i-1] ==  0 ):
                dp[0][i] = 0
            else:
                dp[0][i] = 1
        

        

        for i in range(1,ROWS):
            for j in range(1,COLS):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[ROWS-1][COLS-1]