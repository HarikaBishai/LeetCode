class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stk = []
        out = []
        intervals.sort()
        for start, end in intervals:
            if not stk or stk[-1][1] < start:
                stk.append([start, end])

            else:
                stk_s, stk_e = stk.pop()
                stk.append([stk_s, max(stk_e, end)])
        return stk