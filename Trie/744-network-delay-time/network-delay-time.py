class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        graph = {i+1:[] for i in range(n) }

        for u,v,w in times:
            graph[u].append((v,w))


        

        dist = [float('inf')]*n
        dist[k-1] = 0
        h = [(0,k)]

        while h:
            nodeDist, node = heapq.heappop(h)
            for nei, neiDist in graph[node]:
                if nodeDist + neiDist < dist[nei-1]:
                    dist[nei-1] = nodeDist + neiDist
                    heapq.heappush(h,(dist[nei-1], nei))
        maxDist = max(dist)
        return -1 if maxDist == float('inf') else maxDist