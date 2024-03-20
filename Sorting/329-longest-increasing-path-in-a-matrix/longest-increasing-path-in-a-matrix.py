class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows , cols = len(matrix), len(matrix[0])


        dp = {}

        def dfs(r,c, prevValue):
            if matrix[r][c] <= prevValue:
                return 0

            if (r, c) in dp:
                return dp[(r,c)]
            
            
            directions = [(-1,0), (1,0), (0, -1), (0,1)] 
            res = 1

            dfs_max = 0
            for dir in directions:
                new_r = r+dir[0]
                new_c = c+dir[1]

                if new_r in range(rows) and new_c in range(cols):
                    dfs_max = max(dfs_max, dfs(new_r, new_c, matrix[r][c]))
                
            res = max(res, 1+dfs_max)
            dp[(r,c)] = res
            return res



        for r in range(rows):
            for c in range(cols):
                if (r,c) not in dp: 
                    dp[(r,c)] = dfs(r,c, -1)

        print(dp)
        return max(dp.values())