class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {0:1}
        
        for i in range(1,target+1):
            dp[i] = 0
            for j in nums:
                dp[i] += 0 if i-j not in dp else dp[i-j]
        return dp[target] 
                