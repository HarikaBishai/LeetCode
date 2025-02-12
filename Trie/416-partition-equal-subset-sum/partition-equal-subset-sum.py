class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2:
            return False

        subset_sum = total_sum//2

        dp = [[False]*(subset_sum+1) for _ in range(n+1)]

        

        
        dp[0][0] = True

        for i in range(1, n+1):
            for j in  range(subset_sum+1):

                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                
        return dp[n][subset_sum]


        def dfs(sum, i):
            if sum == 0:
                return True
            if i <= 0 or sum < 0:
                return False
            if nums[i-1] > sum:
                return dfs(sum, i-1)
            return dfs(sum-nums[i-1], i-1) or dfs(sum, i-1)
        
        return dfs(int(total_sum/2), n)

