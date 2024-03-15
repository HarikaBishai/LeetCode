class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # dp = [False] * len(nums)

        # dp[-1] = True

        # for i in range(len(nums)-2, -1, -1):
        #     max_reach = i + nums[i]
        #     for j in range(i+1, max_reach+1):
        #         if dp[j]:
        #             dp[i] = True
        #             break
        
        # return dp[0]


        max_reach = 0
        target = len(nums)-1
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i+jump)
            if max_reach >= target:
                return True

        return False 
    
        