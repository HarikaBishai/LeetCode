class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0


        intervals.sort()

        heap = []

        for start, end in intervals:
            print(heap)
            if not heap or heap[0] > start:
                heapq.heappush(heap,end)
                rooms+=1
            else:
                alloted_room = heapq.heappop(heap)
                heapq.heappush(heap,end)
        return rooms