class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0]*(i+1) for i in range(m)]
        print(dp)
        for i in range(m):
            for j in range(i+1):
                if i == 0 and j==0:
                    dp[i][j] = triangle[i][j]
                    continue
                up = float('inf')
                if i > 0 and j in range(i):
                    print(i-1,j)
                    up = dp[i-1][j]
                upleft = float('inf')
                if i > 0 and j in range(1, i+1):
                    upleft = dp[i-1][j-1]
                dp[i][j] = min(up, upleft) + triangle[i][j]
        print(dp)
        return min(dp[-1])