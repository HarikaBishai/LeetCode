class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m  = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        def dfs(r,c):
            if r == 0 and c == 0:
                return grid[r][c]
            if r<0 or c <0:
                return float('inf')
            if dp[r][c] != -1:
                return dp[r][c]
            up = grid[r][c] + dfs(r-1,c)
            left = grid[r][c] + dfs(r, c-1)
            dp[r][c] = min(up, left)
            return dp[r][c]
        
        return dfs(m-1, n-1)