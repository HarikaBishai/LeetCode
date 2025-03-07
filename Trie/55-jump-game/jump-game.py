class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        
        n = len(nums)
        dp = [False]*n
        dp[0] = True
        farthest = 0
        for i in range(n):
            if dp[i] and i + nums[i] > farthest:
                for j in range(farthest+1, min(n, i+nums[i]+1)):
                    if j >= n-1:
                        return True
                    
                    dp[j] = True
                farthest = max(farthest, i + nums[i])
                
        return False
                
