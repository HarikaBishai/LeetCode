class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        if not nums or nums[0]>target or nums[-1]<target: return [-1,-1]
        leftBound = float('inf')


        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] >= target:
                leftBound = min(leftBound, m)
                r=m-1
            elif nums[m] < target:
                l=m+1
        

        if nums[leftBound]!=target: return [-1,-1]

        rightBound = -1


        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] <= target:
                rightBound = max(rightBound, m)
                l=m+1
            elif nums[m] > target:
                r=m-1

        return [leftBound, rightBound]
        
