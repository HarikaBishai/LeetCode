class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            correct_index = nums[i] - 1

            if 0<nums[i] <= n and nums[i]!=nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i+=1
        

        for i in range(n):
            if nums[i]!= i+1:
                return i+1

        return n+1