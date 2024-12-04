class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}

        m = len(matrix)
        n = len(matrix[0])

        maxSum = 0

        def dfs(i, j, prevValue):
            if matrix[i][j] <= prevValue:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            res = 1

            dir = [(-1,0),(0,1),(1,0),(0,-1)]

            for r, c in dir:
                new_r = i + r
                new_c = j + c

                if new_r in range(m) and new_c in range(n):
                    res = max(res, 1+ dfs(new_r, new_c, matrix[i][j]))

            dp[(i,j)] = res
            return res


        for i in range(m):
            for j in range(n):
                if (i,j) not in dp:
                    maxSum = max(maxSum, dfs(i, j, -1))

        return maxSum