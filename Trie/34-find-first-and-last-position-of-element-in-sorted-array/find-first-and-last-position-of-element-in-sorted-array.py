class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        upperBound = -1

        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m]<=target:
                upperBound = m
                l=m+1
            else:
                r=m-1

        print(upperBound)
        if upperBound == -1 or nums[upperBound]!= target:
            return [-1, -1]

        l = 0
        r = upperBound
        lowerbound = upperBound
        while l<=r:
            m = (l+r)//2
            if nums[m]>= target:
                lowerbound = m
                r=m-1
            else: l= m+1
        
        return [lowerbound, upperBound]