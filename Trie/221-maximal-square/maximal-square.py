class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0]) 
        cache = {}

        dp = [[1 if matrix[j][i] == '1' else 0 for i in range(COLS)] for j in range(ROWS) ]

        print(dp)
        
        for i in range(ROWS-1,-1,-1):
            for j in range(COLS-1, -1, -1):

                if i+1 < ROWS and j+1 < COLS and dp[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        

        maxValue = 0
        for i in range(ROWS):
            for j in range(COLS):
                maxValue = max(maxValue, dp[i][j])
                   

        # def helper(r, c):

        #     if r not in range(ROWS) or c not in range(COLS):
        #         return 0
            
        #     if (r,c) not in cache:
                
        #         down = helper(r+1,c)
        #         right = helper(r, c+1)
        #         diag = helper(r+1, c+1)

        #         cache[(r,c)] = 0

        #         if matrix[r][c] == '1':
        #             cache[(r,c)] = 1 + min(down, right, diag)
        #     return cache[(r,c)]
     

        # helper(0,0)
        return maxValue ** 2