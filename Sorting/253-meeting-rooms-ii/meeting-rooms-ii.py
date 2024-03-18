class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        h = [intervals[0][1]]
        print(intervals)
        heapq.heapify(h)
        out = 1
 
        for i in range(1,len(intervals)):
            if h[0] <= intervals[i][0]:
                heapq.heapreplace(h, intervals[i][1])
            else:
                heapq.heappush(h, intervals[i][1])
                out+=1
            print(h)

        return out
        
        