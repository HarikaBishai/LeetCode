class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stk = []
        intervals.sort()
        for start, end in intervals:
            if not stk or stk[-1][1] < start:
                stk.append([start, end])
                continue
            else:
                s, e = stk.pop()
                stk.append([s, max(e,end)])
        return stk