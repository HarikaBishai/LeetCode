class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        def getMaxRobVal(nums):

            rob1 = 0
            rob2 =  0

            for i in range(len(nums)):
                temp = max(rob2, rob1 + nums[i])
                rob1 = rob2
                rob2 = temp

            return max(rob1, rob2)
        return max(getMaxRobVal(nums[1:]), getMaxRobVal(nums[:len(nums)-1]))