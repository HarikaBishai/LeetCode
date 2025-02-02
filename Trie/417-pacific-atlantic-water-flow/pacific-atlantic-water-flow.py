class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        ROWS = len(heights)
        COLS = len(heights[0])

        pac_set = set()
        alt_set = set()

        def dfs(r,c, seen):
            seen.add((r,c))

            dir = [(-1,0),(0,-1),(0,1),(1,0)]
            for i , j in dir:
                new_r = r + i
                new_c = c + j

                if new_r in range(ROWS) and new_c in range(COLS) and heights[new_r][new_c] >= heights[r][c]  and (new_r, new_c) not in seen:
                    dfs(new_r, new_c, seen)

        for i in range(ROWS):
            dfs(i, 0, pac_set)
            dfs(i, COLS-1, alt_set)

        for i in range( COLS):
            dfs(0, i, pac_set)
            dfs(ROWS-1, i, alt_set)

        print(pac_set, alt_set)
        return list(pac_set & alt_set)