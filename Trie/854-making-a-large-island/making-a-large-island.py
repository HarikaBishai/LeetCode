class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])


        islands_map = {}
        islands = 0
        visited = set()

        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        def dfs(r,c, island_id):
            grid[r][c] = island_id
            nonlocal area
            area +=1
            visited.add((r,c))
            for i, j in dir:
                new_r = i + r
                new_c = j + c
                if 0 <= new_r <= ROWS-1 and 0 <= new_c <= COLS-1 and (new_r,new_c) not in visited and grid[new_r][new_c] == 1:
                    dfs(new_r, new_c, island_id)


        island_id = 2
    
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = 0
                    dfs(i,j, island_id)
                    maxArea = max(area, maxArea)
                    islands_map[island_id] = area
                    island_id+=1
                    islands+=1

        if islands == 0: return 1
        if islands == 1:  return maxArea + 1 if maxArea != ROWS * COLS else maxArea

        print(islands_map, grid)
        maxArea = 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    area = 1
                    neighbouring_islands = set()
                    for i, j in dir:
                        new_r = i + r
                        new_c = j + c
                        if 0 <= new_r <= ROWS-1 and 0 <= new_c <= COLS-1 and grid[new_r][new_c] > 1 and grid[new_r][new_c] not in neighbouring_islands:

                            area += islands_map[grid[new_r][new_c]]
                            neighbouring_islands.add(grid[new_r][new_c])
                    maxArea = max(maxArea, area)

        return  maxArea

                    









        # ones = set()
        # dir = [(-1,0),(1,0),(0,1),(0,-1)]
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1:
        #             ones.add((r,c))
        #             for i, j in dir:
        #                 new_r = i + r
        #                 new_c = j + c
        #                 if 0 <= new_r <= ROWS-1 and 0 <= new_c <= COLS-1 and grid[new_r][new_c] == 0 and (new_r, new_c) not in zeros :
        #                     zeros.add((new_r,new_c))
                            

        
        # if not zeros and ones:
        #     return ROWS*COLS

        
      


        # maxArea = 0
        # for r, c in list(zeros):
        #     area = 0
        #     dfs(r, c, set())
        #     if area > maxArea:
                
        #         maxArea = area
        # return 1 if grid and not zeros else maxArea



