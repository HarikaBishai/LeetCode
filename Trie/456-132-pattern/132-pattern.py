class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        currMin = nums[0]
        for i in nums[1:]:
            while stk and stk[-1][0] <= i:
                stk.pop()
            
            if stk and i > stk[-1][1]:
                return True
            
            stk.append((i,currMin))
            currMin = min(currMin, i)
            

        return False