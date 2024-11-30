class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac = set()
        atl = set()


        def dfs(r,c,visit, prev):
            visit.add((r,c))

            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            for i , j in directions:
                new_r = r + i
                new_c = c + j

                if new_r in range(ROWS) and new_c in range(COLS) and (new_r, new_c) not in visit and heights[new_r][new_c] >= prev:
                    dfs(new_r,new_c, visit, heights[new_r][new_c])

        for c in range(COLS):
            dfs(0, c , pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0 , pac, heights[r][0])
            dfs(r, COLS-1 , atl, heights[r][COLS-1])

        result = []
        print(pac, atl)
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    result.append([i,j])

        return result
