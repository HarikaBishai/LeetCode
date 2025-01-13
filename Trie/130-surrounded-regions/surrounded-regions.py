class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        


        ROWS = len(board)
        COLS = len(board[0])


        def dfs(r,c ):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != 'O':
                return
            board[r][c] ='T'
            dfs(r+1,c )
            dfs(r-1,c )
            dfs(r,c+1 )
            dfs(r,c-1 )


        for i in range(ROWS):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][COLS-1] == 'O':
                dfs(i, COLS-1)
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1, c) 
            
            
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'T':
                    board[i][j] = 'O'


         

