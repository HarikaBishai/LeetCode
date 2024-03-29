class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        h = [intervals[0][1]]
        heapq.heapify(h)
        out = 1
 
        for i in range(1,len(intervals)):
            if h[0] <= intervals[i][0]:
                heapq.heapreplace(h, intervals[i][1])
            else:
                heapq.heappush(h, intervals[i][1])
                out+=1

        return out
        
        