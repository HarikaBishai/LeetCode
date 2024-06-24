class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0
        m = len(grid)
        n = len(grid[0])
        print(m, n)
        visited = [[0 for _ in range(n)] for _ in range(m)]

        print(visited)
        def dfs(i, j):
            visited[i][j] = 1
            dir = [(-1, 0), (1,0), (0,-1), (0,1)]

            for r, c in dir:
                new_r = i + r
                new_c = j + c
                if new_r in range(0, m) and new_c in range(0, n) and grid[i][j] == '1' and not visited[new_r][new_c]:
                    dfs(new_r, new_c)

            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i,j)
                    out+=1
        return out
            