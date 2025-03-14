class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0

        r = len(nums)-1
        ans = len(nums)

        while l<=r:
            m = (l+r)//2

            if nums[m] >= target:
                ans = min(ans, m)
                r-=1
            else:
                l+=1
        return ans