class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()
        fresh , time = 0, 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 1:
                    fresh+=1
                else:
                    q.append((i,j))
                    visited.add((i,j))


        while q and fresh > 0:

            for _ in range(len(q)):
                r,c = q.popleft()

                directions = [(-1,0),(1,0),(0,-1),(0,1)]


                for i, j in directions:
                    new_r = r + i
                    new_c = c + j
                    if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        grid[new_r][new_c] = 2
                        q.append((new_r, new_c))
                        fresh-=1

            
            time+=1
        return time if fresh == 0 else -1
