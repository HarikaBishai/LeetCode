class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h = []

        for x, y in points:
            dis = -(x**2 + y**2)
            if len(h) == k:
                heapq.heappushpop(h,(dis, (x, y)))
            else:
                heapq.heappush(h,(dis, (x, y)))
            
        out = []
        for dis, point in h:
            out.append(point)
        return out