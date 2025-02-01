class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        # dp = [float('inf')]*n
        # dp[src] = 0

        # for i in range(k+1):
        #     new_dp = dp.copy()

        #     for u, v , w in flights:
        #         if dp[u] != float('inf') and dp[u]+w < new_dp[v]:
        #             new_dp[v] = dp[u]+w
        #     dp = new_dp

        # return -1 if dp[dst] == float('inf') else dp[dst]



        graph = defaultdict(list)

        for u, v , w in flights:
            graph[u].append((v,w))

        heap = [(0, src, 0)]

        best = dict()


        while heap:
            dist, city, stops = heapq.heappop(heap)
            if city == dst:
                return dist
            
            if stops <= k:
                for nei, w in graph[city]:
                    if (nei, stops+1) not in best or best[(nei, stops+1)] > dist+w:
                        best[(nei, stops+1)] = dist+w
                        heapq.heappush(heap, (dist+w, nei, stops+1))

        return -1
