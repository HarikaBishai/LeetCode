class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = []

        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            else:
                bricks = bricks - diff
                heapq.heappush(maxHeap, -diff)

                if bricks < 0:
                    if ladders == 0:
                        return i
                    bricks+= -heapq.heappop(maxHeap)
                    ladders-=1
                
        return len(heights)-1