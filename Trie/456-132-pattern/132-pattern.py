class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        currMin = nums[0]

        for num in nums[1:]:
            while stk and num >= stk[-1][0]:
                stk.pop()
            
            if stk and num > stk[-1][1] :
                return True
            
            stk.append((num, currMin))
            currMin = min(num, currMin)
        return False
