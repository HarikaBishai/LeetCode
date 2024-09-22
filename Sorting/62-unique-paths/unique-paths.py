class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]

        def dfs(r,c):
            if r == 0 and c == 0:
                return 1
            if r<0 or c<0:
                return 0
            if dp[r][c] !=-1:
                return dp[r][c]
            
            up = dfs(r-1,c)
            left = dfs(r,c-1)

            dp[r][c] = up+left
            return dp[r][c]

        return dfs(m-1, n-1)