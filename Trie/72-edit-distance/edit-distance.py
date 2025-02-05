class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        
        
        # def getMin(i, j):
        #     if i == len(word1):
        #         return len(word2)-j
        #     if j == len(word2):
        #         return len(word1)-i

        
        #     if word1[i] == word2[j]:
        #         return getMin(i+1, j+1)
            
        #     return 1 + min(getMin(i, j+1), getMin(i+1, j+1), getMin(i+1, j))
        
        
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        

        for i in range(n1+1):
            for j in range(n2+1):
                if j == 0:
                    dp[i][j] = i
                elif i == 0:
                    dp[i][j] = j
                else:

                    if word1[i-1] == word2[j-1]:
                        dp[i][j] =  dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        print(dp)
        return dp[n1][n2] if dp else 0