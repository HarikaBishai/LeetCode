class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        dp = [[0]* COLS for _ in range(ROWS)]

        dp[0][0] = grid[0][0]
        for i in range(1,COLS):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for i in range(1,ROWS):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        
        for i in range(1,ROWS):
            for j in range(1,COLS):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[ROWS-1][COLS-1]