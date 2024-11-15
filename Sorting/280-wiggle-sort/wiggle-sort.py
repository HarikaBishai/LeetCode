class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        flag = False
        for i in range(1, len(nums)):
            if (not flag) and nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            elif flag and nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        
            flag =  not flag
        
        return nums


        