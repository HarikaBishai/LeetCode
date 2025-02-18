class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        i = 0
        while i < n+1:
            if i not in nums:
                return i
            i+=1
        return n+1