class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        

        graph = defaultdict(list)


        for u, v , w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        q = deque([1])
        visited = set([1])


       

        
        out = float('inf')
        while q:
            city = q.popleft()

            

            # if city in visited:
            #     continue
            # visited.add(city)


            for nei, sc in graph[city]:
                out = min(sc, out)
                if nei not in visited:
                    
                    q.append(nei)
                    visited.add(nei)
                

                
                
        return out

        
