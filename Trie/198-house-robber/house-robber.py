class Solution:
    def rob(self, nums: List[int]) -> int:
        # max_rob_amount = 0
        # if len(nums)<2:
        #     return max(nums)

        # else:
        #     stack = [(0,nums[0]), (1, nums[1])]
            
        #     while stack:
        #         index, curr_amount = stack.pop()
        #         max_rob_amount = max(curr_amount, max_rob_amount)
        #         for i in range(index+2, len(nums)):
        #             stack.append((i, curr_amount+nums[i]))


        # return max_rob_amount

        # if not nums:
        #     return 0

        # dp = [None]*(len(nums)+1)
        # n = len(nums)

        # dp[n], dp[n-1] = 0, nums[n-1]

        
        # for i in range(n-2, -1,-1):
        #     dp[i] = max(dp[i+1], dp[i+2] + nums[i])

        # return dp[0]   

        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i])

        return max(dp[-1], dp[-2])