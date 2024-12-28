class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stk = []
        out = []
        l = 0
        for i in range(len(nums)):
            while stk and  stk[-1][1] < nums[i]:
                stk.pop()

            stk.append((i, nums[i]))
 

            if i >= k-1:
                out.append(stk[0][1])
            
            if stk and stk[0][0] <= i-k+1:
                stk.pop(0)
        
        return out


