class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {
            0: -1
        }

        total = 0
        for i in range(len(nums)):
            total += nums[i]
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] >= 2:
                return True
            
        return False
