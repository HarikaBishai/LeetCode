class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        

        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1


        best = {(0,0): 1}
        
        h = [(1,0,0)]

        while h:
            dist, r, c = heapq.heappop(h)
            
           
            if r == ROWS-1 and c == COLS-1:
                return dist
            
            dir = [(-1,0), (1,0), (0,-1), (0, 1), (1, -1),(1, 1), (-1, 1), (-1, -1)]

            for i, j in dir:
                new_r = r + i
                new_c = c + j

                if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 0 and (new_r, new_c) not in best:
                    best[(new_r, new_c)] = dist+1

                    heapq.heappush(h, (dist+1, new_r, new_c))
        return -1
