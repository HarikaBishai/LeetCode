class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []

        for x, y in points:
            distances.append(x**2 + y**2)

        
        minHeap = []
        for i , point in enumerate(points):
            
            heapq.heappush(minHeap,(-distances[i], point))
            if i>= k:
                heapq.heappop(minHeap)
        

        out = []

        while minHeap:
            distance, point = heapq.heappop(minHeap)
            out.append(point)
        return out


