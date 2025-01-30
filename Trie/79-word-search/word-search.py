class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
       
        path = set()


        def dfs(r, c, k):

            if word[k] != board[r][c]:
                return False
            
            path.add((r,c))

            if len(path) == len(word):
                return True
            
            

            
           
            dir = [(-1,0),(1,0), (0,1), (0,-1)]

            for i , j in dir:
                new_r = i + r
                new_c = j + c

                if new_r in range(ROWS) and new_c in range(COLS) and (new_r, new_c) not in path:
                    if dfs(new_r, new_c, k+1):
                        return True



            path.remove((r,c))
            return False


        for i in range(ROWS):
            for j in range(COLS):
                if  dfs(i,j, 0):
                    return True
        return False

