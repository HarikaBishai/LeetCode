class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
       
        currSum = 0
        minLength = float('inf')
        for i in range(len(nums)):
            currSum += nums[i]
           

            while currSum >= target:
                minLength = min(minLength, i-l+1)
                currSum -= nums[l]
                l = l+1
        
         
        return 0 if minLength == float('inf') else minLength