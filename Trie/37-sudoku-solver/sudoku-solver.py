class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        n = len(board)
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    v = int(board[i][j])
                    rows[i].add(v)
                    cols[j].add(v)
                    squares[(i//3, j//3)].add(v)

        def isValid(r, c, k):

            return not(k in rows[r] or k in cols[c] or k in squares[(r//3, c//3)]) 


        def backtrack(r, c):
            if r == n-1 and c == n:
                return True
            elif c == 9:
                c = 0
                r = r+1
            
            if board[r][c]!='.':
                return backtrack(r,c+1)

            for v in range(1, n+1):
                if not isValid(r, c, v):
                    continue
                board[r][c]=str(v)
                rows[r].add(v)
                cols[c].add(v)
                squares[(r//3, c//3)].add(v)

                if backtrack(r, c+1):
                    return True
                board[r][c]='.'
                rows[r].remove(v)
                cols[c].remove(v)
                squares[(r//3, c//3)].remove(v)

            return False
        
        backtrack(0,0)
            

        
        