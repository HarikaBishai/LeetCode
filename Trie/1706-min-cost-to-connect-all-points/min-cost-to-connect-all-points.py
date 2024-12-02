class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append((j, dist))
                graph[j].append((i, dist))

        q=deque([(0, 0)])

        h = [(0,0)]
        
        res = 0
        visited = set()
        while h:
            dist, point = heapq.heappop(h)
            if point in visited:
                continue
            visited.add(point)

            res+=dist

            for nei, wt in graph[point]:
                if nei not in visited:
                    heapq.heappush(h,(wt, nei))

            
        return res