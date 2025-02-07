class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = {0: -1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix = (prefix + num) % k
            if prefix in prefix_mod:
                if i-prefix_mod[prefix]>1:
                    return True
            else:
                prefix_mod[prefix] = i
        return False
