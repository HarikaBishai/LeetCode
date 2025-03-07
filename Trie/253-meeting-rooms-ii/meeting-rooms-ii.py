class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        hp = []
        out = 0

        for st, end in intervals:
            if hp and hp[0] <= st:
                heapq.heappushpop(hp, end)
            else:
                out+=1
                heapq.heappush(hp, end)
        return out