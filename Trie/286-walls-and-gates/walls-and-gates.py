class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        

        ROWS = len(rooms)
        COLS = len(rooms[0])




        q = deque()
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        level = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                dir = [(-1,0),(1,0),(0,1),(0,-1)]
                for i, j in dir:
                    new_r = r+i
                    new_c = c+j
                    if new_r in range(ROWS) and new_c in range(COLS) and (new_r, new_c) not in visited and rooms[new_r][new_c] != -1:
                        q.append((new_r, new_c))
                        rooms[new_r][new_c] = level
                        visited.add((new_r, new_c))
            level+=1

        return rooms

