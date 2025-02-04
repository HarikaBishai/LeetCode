class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i: [] for i in range(1, n+1)}


        for u, v, t in times:
            graph[u].append((v, t))

        
        print(graph)
        p_q = [(0,k)]

        visited = set()
        time = 0
        while p_q:
            t, node = heapq.heappop(p_q)
            if node in visited:
                continue
            visited.add(node)
            time = t
            for nei, nei_t in graph[node]:
                if nei not in visited:
                    heapq.heappush(p_q, (time + nei_t, nei))
                    
    
        return time if len(visited) == n else -1

