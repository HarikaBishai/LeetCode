class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        perimeter = 0


        def dfs(r,c):
            nonlocal perimeter
            visited.add((r,c))

            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            for i , j in directions:
                new_r = r + i
                new_c = c + j

                if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                    dfs(new_r, new_c)
                    
                elif (new_r, new_c) not in visited:
                    perimeter+=1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    dfs(i,j)
                    return perimeter
        
        