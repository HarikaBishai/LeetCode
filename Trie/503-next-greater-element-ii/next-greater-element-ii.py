class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []


        n = len(nums)
        out = [-1]*n

        for i in range(2*n):
            while stk and nums[stk[-1]] < nums[i%n]:
                index = stk.pop()
                out[index] = nums[i%n]
            
            if i<n:
                stk.append(i%n)
        return out