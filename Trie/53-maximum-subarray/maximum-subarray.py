class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curr_sum = float('-inf')
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            maxSum = max(curr_sum, maxSum)
        return maxSum