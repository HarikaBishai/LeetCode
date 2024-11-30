class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        q = deque()

        ROWS = len(rooms)
        COLS = len(rooms[0])

        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        dist = 0

        def addRoom(r, c, q):
            if r in range(ROWS) and c in range(COLS) and (r,c) not in visited and rooms[r][c] != -1:
                visited.add((r,c))
                q.append((r,c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
            
                addRoom(r+1, c, q)
                addRoom(r-1, c, q)
                addRoom(r, c+1, q)
                addRoom(r, c-1, q)
            dist +=1

        return dist




            
            
        