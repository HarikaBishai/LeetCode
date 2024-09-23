class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m  = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                    continue
                up = float('inf')
                if r>0:
                    up= dp[r-1][c]
                left = float(inf)
                if c>0:
                    left = dp[r][c-1]
                dp[r][c] = grid[r][c] +  min(up, left)
            
        
        return dp[m-1][n-1]