class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        
        for i, num in enumerate(nums):
            if (target-num) in diff:
                return [i, diff[(target-num)]]
            else:
                diff[num] = i
        return []