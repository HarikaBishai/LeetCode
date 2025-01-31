class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(mat)
        COLS = len(mat[0])
        
        
        out = [[float('inf')]*COLS for _ in range(ROWS)]
        q = deque()
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
                    out[i][j] = 0
        level = 1
        while q:
            print(q)
            for _ in range(len(q)):
                r, c = q.popleft()

                dir = [(-1, 0),(1,0),(0,-1),(0,1)]

                for i, j in dir:
                    new_r = i + r
                    new_c = j + c

                    if new_r in range(ROWS) and new_c in range(COLS) and (new_r, new_c) not in visited:
                        out[new_r][new_c] = level
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
            level+=1
        print(visited)
        return out



