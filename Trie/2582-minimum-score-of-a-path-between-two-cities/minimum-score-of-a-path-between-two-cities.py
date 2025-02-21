class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        

        graph = defaultdict(list)


        for u, v , w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        q = deque([1])
        visited = set([1])


        out = float('inf')
        def dfs(node):
            nonlocal out
            for nei, dist in graph[node]:
                out = min(dist, out)
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        dfs(1)
        return out

        
        out = float('inf')
        while q:
            city = q.popleft()


            for nei, sc in graph[city]:
                out = min(sc, out)
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
                

                
                
        return out

        
