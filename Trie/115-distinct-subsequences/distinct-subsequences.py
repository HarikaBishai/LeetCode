class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        M = len(s)
        N = len(t)
        # def dfs(i, j):
        #     if i == M or j == N:
        #         return 1 if j == N else 0

            
        #     if s[i] == t[j]:
        #         return dfs(i+1, j) + dfs(i+1, j+1)
        #     else:
        #         return dfs(i+1, j)
        # return dfs(0,0)
                

        
        dp = [[0]*(N+1) for _ in range(M+1)]

        for i in range(M+1):
            dp[i][N] = 1


        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                dp[i][j] = dp[i+1][j]

                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]