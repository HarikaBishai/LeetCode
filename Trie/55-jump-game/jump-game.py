class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)<=1:
            return True

        n = len(nums)
        dp = [False] * len(nums)
        dp[0] = True

        farthest = 0
        for i in range(len(nums)):
            if dp[i] :
                if i + nums[i] >= n-1:
                    return True
                if i + nums[i] > farthest:
                    
                    for j in range(farthest+1,i+nums[i]+1):
                        dp[j] = True
                    farthest = i + nums[i]
        return dp[n-1]