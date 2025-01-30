class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0
        intervals.sort()
        heap = []

        for start, end in intervals:
            if not heap or heap[0] > start:
                heapq.heappush(heap,end)
                rooms+=1
            else:
                heapq.heappushpop(heap, end)
        return rooms