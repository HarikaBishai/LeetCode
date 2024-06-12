class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf') for i in range(n)]
        dist[src] = 0

        for i in range(k+1):
            temp = dist[:]
            for u,v,w in flights:
                if dist[u] != float('inf'):
                    temp[v] = min(temp[v], dist[u]+w)
            dist = temp
        return -1 if dist[dst] == float('inf') else dist[dst]

        