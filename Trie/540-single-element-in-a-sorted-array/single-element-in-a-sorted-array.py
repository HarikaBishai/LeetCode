class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 1
        r = len(nums)-2
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid-1]!= nums[mid] and nums[mid+1]!=nums[mid]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid]!=nums[mid+1]:
                    r=mid-1
                else:
                    l=mid+1

            else:
                if nums[mid-1]!=nums[mid]:
                    r=mid-1
                else:
                    l = mid+1
        return -1