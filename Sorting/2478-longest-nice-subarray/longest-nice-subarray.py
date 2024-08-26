class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        num = 0
        l, r = 0, 0
        max_len = 0

        while r < len(nums):
            while num & nums[r] !=0 :
                num ^= nums[l]
                l+=1
            num |= nums[r]
            max_len = max(max_len, r-l+1)
            r+=1
        return max_len

        