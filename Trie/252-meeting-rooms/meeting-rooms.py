class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        stk = []

        for st, end in intervals:
            if not stk or stk[-1][1] <= st:
                stk.append([st,end])
            else:
                return False
        return True