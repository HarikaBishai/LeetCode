class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        def dfs(r,c, area):

            visited.add((r,c))
            area+=1
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for i, j in directions:
                new_r = r + i
                new_c = c + j
                if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 1 and  (new_r, new_c) not in visited:
                    area = dfs(new_r, new_c, area)
            
            return area
        
        cnt = 0
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = dfs(i,j, 0)
                    maxArea = max(maxArea, area)
                    
                
        return maxArea