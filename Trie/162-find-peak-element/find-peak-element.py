class Solution:
    def findPeakElement(self, nums: List[int]) -> int:


        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        l = 1
        r = n-2

        while l<=r:
            mid = (l+r)//2

            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid-1] < nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1
        # if len(nums) <= 1:
        #     return 0
        # for i in range(len(nums)):
        #     if i == 0:
        #         if len(nums)>1 and nums[i] > nums[i+1]:
        #             return i

        #     elif i == len(nums)-1:
        #         if nums[i] > nums[i-1]:
        #             return i
        #     else:
        #         if nums[i-1] < nums[i] > nums[i+1]:
        #             return i

        # return None