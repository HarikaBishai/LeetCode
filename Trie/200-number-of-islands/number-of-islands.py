class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()


        no_of_islands = 0

        def dfs(r,c):
            visited.add((r,c))


            dir = [(-1,0), (1, 0),(0,1),(0,-1)]

            for i, j in dir:
                new_r = i + r
                new_c = j + c

                if new_r in range(ROWS) and new_c in range(COLS) and (new_r, new_c) not in visited and grid[new_r][new_c] == '1':
                    dfs(new_r, new_c)


            

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j)
                    no_of_islands +=1
        return no_of_islands

    



