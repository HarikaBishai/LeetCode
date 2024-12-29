class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)

        stk = []

        for i, temp in enumerate(temperatures):
            
            while stk and stk[-1][1] < temp:
                idx, top = stk.pop()
                ans[idx] = i-idx
            stk.append((i, temp))
        return ans
