class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1]!= nums[-2]:
            return nums[-1]

        l = 1
        r = len(nums)-2
        while l<=r:
            m = (l+r)//2

            if nums[m]!= nums[m-1] and nums[m]!= nums[m+1]:
                return nums[m]
            if m%2 == 0:
                if nums[m] != nums[m+1]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] != nums[m-1]:
                    r = m-1
                else:
                    l = m+1
        return -1