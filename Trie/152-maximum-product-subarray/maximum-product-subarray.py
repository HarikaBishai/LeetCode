class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_min = nums[0]
        curr_max = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            temp = max(curr_min*nums[i], curr_max*nums[i], nums[i])
            curr_min = min(curr_min*nums[i], curr_max*nums[i], nums[i])
            curr_max = temp
            max_product = max(curr_max, max_product)
        return max_product