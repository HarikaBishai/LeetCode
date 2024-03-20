class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        islands = 0
        visited = set()


        def dfs(r,c):
            visited.add((r,c))
            
            directions = [(-1,0),(1,0),(0,1),(0,-1)]

            for dir in directions:
                new_r = r + dir[0]
                new_c = c + dir[1]
                if new_r in range(rows) and new_c in range(cols) and (new_r, new_c) not in visited and grid[new_r][new_c] == '1':
                    dfs(new_r, new_c)
        


        for r in range(rows):
            for c in range(cols):
                if  grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands+=1

        return islands
