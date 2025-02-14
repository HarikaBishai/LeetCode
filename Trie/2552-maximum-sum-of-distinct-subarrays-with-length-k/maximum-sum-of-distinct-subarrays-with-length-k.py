class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        maxSum = 0
        l = 0
        window = set()
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            while nums[i] in window or len(window) >= k:
                window.remove(nums[l])
                curr_sum-= nums[l]
                l+=1
            window.add(nums[i])
            if len(window) == k:
                maxSum = max(maxSum, curr_sum)
        
        return maxSum
        


