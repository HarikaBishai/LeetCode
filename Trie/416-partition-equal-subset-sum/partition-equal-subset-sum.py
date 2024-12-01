class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False



        target = sum(nums)//2

        dp = [[False] * (target+1) for _ in range(len(nums)+1)]

        dp[0][0] = True

        for i in range(1,len(nums)+1):
            for j in range(target+1):
                
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else: 
                    dp[i][j] = dp[i-1][j]
        
        return dp[len(nums)][target]

        # dp = set([0])
        # for i in range(len(nums)-1, -1, -1):
        #     numSet = set()
        #     for j in dp:
        #         numSet.add(nums[i]+j)
        #         numSet.add(j)
        #     dp = numSet
        #     if target in numSet:
        #         return True

        # return False