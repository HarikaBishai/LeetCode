class Solution:
    def twoSum(self, nums: List[int], target: int)-> List[int]:
        seenSum = {}

        for i, num in enumerate(nums):
            if num in seenSum:
                return([i, seenSum[num]])
            
            seenSum[target-num] =i

        return []

             