class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0

        maxLen = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            while k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
            maxLen = max(r-l+1, maxLen)
        return maxLen