class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

        ROWS = len(board)
        COLS = len(board[0])
        q = deque()
        seen = set()
        for i in range(ROWS):
            if board[i][0] == "O":
                q.append((i,0))
            if board[i][COLS-1] == "O":
                q.append((i,COLS-1))

        for i in range(COLS):
            if board[0][i] == "O":
                q.append((0,i))
            if board[ROWS-1][i] == "O":
                q.append((ROWS-1,i))

        while q:
            
            r, c = q.popleft()
            if (r,c) in seen:
                continue
            board[r][c] = 'T'
            seen.add((r,c))
            dir = [(-1, 0), (0, -1), (1,0), (0,1)]

            for i , j in dir:
                new_r = i+ r
                new_c = j+ c
                if new_r in range(ROWS) and new_c in range(COLS) and (new_r, new_c) not in seen and board[new_r][new_c] == 'O':
                    q.append((new_r, new_c))
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        