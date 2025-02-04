class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        dp = [[0] * (n2) for _ in range(n1)]
        
        for i in range(n1):
            for j in range(n2):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n1-1][n2-1]
        # def lcs(i, j):
        #     if i >= n1 or j >= n2:
        #         return 0

        #     if text1[i] == text2[j]:
        #         return 1 + lcs(i+1, j+1)
            
        #     return max(lcs(i+1, j), lcs(i, j+1))

        return lcs(0,0)
        