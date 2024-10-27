class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[l]<=nums[r]:
                ans = min(ans, nums[l])
                break
            if nums[l]<=nums[mid]:
                ans = min(ans, nums[l])
                l= mid+1
            else:
                ans = min(ans, nums[mid])
                r=mid-1
        return ans
        