class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        out  = []
        for num in nums:
            n = abs(num)
            if nums[n-1] < 0:
                out.append(n)
            else:
                nums[n-1] = -nums[n-1]
        return out
