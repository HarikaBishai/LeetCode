class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)<=1:
            return True

        n = len(nums)
        dp = [False] * len(nums)
        dp[0] = True

        farthest = 0
        for i in range(len(nums)):
            if dp[i] and i + nums[i] > farthest:
                for j in range(farthest+1,i+nums[i]+1):
                    if j > n-1 or j + nums[j] >= n-1:
                        return True
                    dp[j] = True
                farthest = i + nums[i]
        return dp[n-1]