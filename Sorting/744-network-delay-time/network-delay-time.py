class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        for i in range(1, n+1):
            graph[i] = []
        
        for src, dest, wei in times:
            graph[src].append((wei, dest))
        
        heap = [(0, k)]
        heapq.heapify(heap)
        shortest = {}

        while heap:
            curr_wei, dest = heapq.heappop(heap)

            if dest in shortest:
                continue

            shortest[dest] = curr_wei

            for wei, nei in graph[dest]:
                if nei not in shortest:
                    heapq.heappush(heap,(curr_wei+wei, nei))

        return max(shortest.values()) if len(shortest.keys() ) == n else -1