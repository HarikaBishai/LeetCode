class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk = []
        out = [-1] * len(nums)
        for i in range(2*n):
            i = i% n
            num = nums[i]
            while stk and stk[-1][1] < num:
                idx, val = stk.pop()
                out[idx] = num
            
            stk.append((i, num))

        

                    
        return out
