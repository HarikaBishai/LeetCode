class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols = set()
        posDiag = set()
        negDiag = set()
        board = [["."]*n for _ in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(board[i]) for i in range(n)]
                res.append(copy)
                return
            
            for c in range(n):
                if c not in cols and r+c not in posDiag and r-c not in negDiag:
                    board[r][c] = "Q"
                    cols.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    backtrack(r+1)
                    board[r][c] = "."
                    cols.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)

            
        backtrack(0)
        return res