class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m  = len(board)
        n = len(board[0])
        if not word:
            return False
        def dfs(r, c, index, visited):
            visited.add((r,c))
            index = index+1
            if index == len(word):
                return True
            if index > len (word):
                return False
            dir = [(-1,0), (1,0),(0,-1),(0,1)]

            for k, l in dir:
                new_r = r+k
                new_c = c+l
                if new_r in range(m) and new_c in range(n) and (new_r, new_c) not in visited and word[index] == board[new_r][new_c]:
                    if dfs(new_r, new_c, index, visited) :
                        return True
            
            visited.remove((r, c))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0, set()):
                    return True
        return False

