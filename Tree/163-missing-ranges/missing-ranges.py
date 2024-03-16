class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        out = []
        n = len(nums)

        for i in range(n):
            if lower!=nums[i]:
                out.append([lower, nums[i]-1])
            lower = nums[i] + 1
        
        if lower<=upper:
            out.append([lower, upper])

        
            
        return out