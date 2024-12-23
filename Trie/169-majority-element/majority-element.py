class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = res = 0

        for num in nums:
            if count == 0:
                res = num
                
            count = count + 1 if res == num else count - 1
        
        return res
