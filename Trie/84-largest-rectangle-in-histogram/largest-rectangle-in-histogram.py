class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxArea = float('-inf')
        for i, height in enumerate(heights):
            index = i 
            while stk and stk[-1][1] > height:
                idx, h = stk.pop()
                maxArea = max(maxArea, h * (i-idx))
                index = idx
            stk.append((index,height))
        while stk:
            idx, h = stk.pop()
            maxArea = max(maxArea, h * (len(heights)-idx))
        return maxArea
                

            
