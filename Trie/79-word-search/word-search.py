class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        R = len(board)
        C = len(board[0])

        path = set()

        def dfs(i, r,c):
            if i == len(word):
                return True
            if r not in range(R) or c not in range(C) or word[i]!= board[r][c] or (r,c) in path:
                return False
            
            path.add((r,c))

            res = dfs(i+1, r+1,c) or dfs(i+1, r-1, c) or dfs(i+1, r, c+1) or dfs(i+1, r, c-1)

            path.remove((r,c))

            return res

        
        for i in range(R):
            for j in range(C):
                if dfs(0, i,j):
                    return True
        
        return False