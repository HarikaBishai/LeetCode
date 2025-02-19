class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        sum = float('-inf')
        for i in range(len(nums)):
            

            sum = max(sum+nums[i], nums[i])
            maxSum = max(maxSum, sum)
        return maxSum