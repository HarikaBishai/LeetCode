class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for i in range(k):
            x, y = points[i]
            heapq.heappush(h,(-1*(x**2 + y**2), [x,y]))
        for i in range(k, len(points)):
            x, y = points[i]
            heapq.heappushpop(h,(-1*(x**2 + y**2), [x,y]))
        
        out = []

        while h:
            out.append(heapq.heappop(h)[1])
        return out
