class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums
        # g = 0
        # for i in range(2*l):
        #     if i >= l:
        #         result.append(nums[g])
        #         g += 1
        #     elif i < l:
        #         result.append(nums[i])
        return result
            
        