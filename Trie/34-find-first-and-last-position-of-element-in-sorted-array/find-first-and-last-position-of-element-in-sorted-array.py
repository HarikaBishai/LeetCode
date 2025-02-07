class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        firstPos = -1
        lastPos = -1

        l = 0
        r = len(nums) -1

        while l<=r:
            m = (l+r)//2

            if nums[m] >= target:
                firstPos = m
                r = m-1
            
            else:
                l = m+1
        
        if firstPos == -1 or nums[firstPos] != target:
            return [-1, -1]

        l = 0
        r = len(nums) -1

        while l<=r:
            m = (l+r)//2

            if nums[m] <= target:
                rightPos = m
                l = m+1
            
            else:
                r = m-1
        return [firstPos, rightPos]
        
