class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {}

        for i in range(1,n+1):
            graph[i] = []

        for src,end,wei in times:
            graph[src].append((wei, end))


        shortest = {}
        h = [(0,k)]
        heapq.heapify(h)

        while h:
            w1,n1 = heapq.heappop(h)

            if n1 in shortest:
                continue
            
            shortest[n1] = w1

            for w2, nei in graph[n1]:
                if nei not in shortest:
                    heapq.heappush(h, (w1+w2, nei))
        
        for i in range(1,n+1):
            if i not in shortest:
                return -1
        
        return max(shortest.values())
