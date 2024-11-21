class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []

        out = [0] * len(temperatures)

        for i, val in enumerate(temperatures):
            while stk and stk[-1][0] < val:
                temp, idx = stk.pop()
                out[idx] = i-idx
            stk.append((val, i))

        return out