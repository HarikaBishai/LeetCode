class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True
        if nums[0] == 0 :
            return False
        n = len(nums)
        dp = [False]*n
        dp[0] = True
        farthest = 0
        for i in range(n):
            if nums[i] and dp[i]:
                for j in range(i, min(n, i+nums[i]+1)):
                    if nums[j]:
                        farthest = max(farthest, j + nums[j])
                        if farthest >= n-1:
                            return True
                        dp[j] = True
                
        return False
                
