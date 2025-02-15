class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)<=1:
            return True

        n = len(nums)
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums)):
            if dp[i] :
                if i + nums[i] >= n-1:
                    return True
                for j in range(i+1,i+nums[i]+1):
                    dp[j] = True
        return dp[n-1]