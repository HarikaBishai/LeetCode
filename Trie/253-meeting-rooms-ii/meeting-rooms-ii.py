class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0

        h = []

        intervals.sort()
        for st, end in intervals:
            if not h or h[0] > st:
                heapq.heappush(h, end)
                rooms+=1
            else:
                heapq.heappushpop(h, end)

        return rooms