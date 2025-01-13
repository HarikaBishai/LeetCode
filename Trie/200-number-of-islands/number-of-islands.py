class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        no_of_islands = 0
        def dfs(r,c):

            visit.add((r,c))


            dir = [(-1,0),(1,0),(0,1),(0,-1)]

            for i, j in dir:
                new_r = r+i
                new_c = c+j

                if new_r in range(ROWS) and new_c in range(COLS) and (new_r, new_c) not in visit and grid[new_r][new_c] == "1":
                    dfs(new_r, new_c)
        

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visit and grid[i][j] == "1":
                    dfs(i,j)
                    no_of_islands+=1
                
        
        return no_of_islands

        

