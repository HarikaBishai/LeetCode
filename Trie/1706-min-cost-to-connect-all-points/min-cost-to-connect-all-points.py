class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        N = len(points)

        adj = { i: [] for i in range(N)}


        for i in range(N):
            x, y = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]

                dist = abs(x-x2) + abs(y2-y)
                adj[i].append((j, dist))
                adj[j].append((i,dist))

        
        h = []
        heapq.heappush(h,(0,0))
        time = 0
        visit = set()
        while h:
            dist, node = heapq.heappop(h)

            if node in visit:
                continue
            visit.add(node)
            time+=dist
            for nei, dist2 in adj[node]:
                if nei not in visit:
                    heapq.heappush(h, (dist2, nei))

        return time

