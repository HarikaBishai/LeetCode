class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        



        out = []

        def getPermutate(nums, i):
            if i == len(nums):
                out.append(nums[:])
            for j in range(i,len(nums)):
                
                nums[i],nums[j] = nums[j], nums[i]
                getPermutate(nums, i+1)
                nums[i],nums[j] = nums[j], nums[i]

        getPermutate(nums, 0)

        return out
        

