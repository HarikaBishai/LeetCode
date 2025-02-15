class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)<=1:
            return True
        if nums[0] == 0:
            return False

        n = len(nums)
        dp = [False] * len(nums)
        dp[0] = True
        farthestJump = 0
        for i in range(len(nums)):
            if dp[i] :
                if dp[i] and i + nums[i] >= n-1:
                    return True
                for j in range(i,i+nums[i]+1):
                    dp[j] = True
        print(dp)
        return dp[n-1]