class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0]) 

        dp = [[1 if matrix[j][i] == '1' else 0 for i in range(COLS)] for j in range(ROWS) ]

        
        for i in range(ROWS-1,-1,-1):
            for j in range(COLS-1, -1, -1):

                if i+1 < ROWS and j+1 < COLS and dp[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        

        maxValue = 0
        for i in range(ROWS):
            for j in range(COLS):
                maxValue = max(maxValue, dp[i][j])
                   

        return maxValue ** 2