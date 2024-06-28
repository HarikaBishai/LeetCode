class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        out = len(nums) + 1
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            while curr_sum >= target:
                out = min(i-l+1, out)
                curr_sum-=nums[l]
                l+=1
        return 0 if out == len(nums) + 1 else out


           
