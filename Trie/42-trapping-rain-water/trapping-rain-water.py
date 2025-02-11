class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        res = 0
        for i in range(len(height)):
            while stk and height[stk[-1]] < height[i]:

                mid = stk.pop()
                if stk:
                    left = height[stk[-1]]
                    right = height[i]
                    h = min(left, right) - height[mid]
                    w = i-stk[-1] -1
                    print(h,w)
                    res += w*h
            stk.append(i)
        return res