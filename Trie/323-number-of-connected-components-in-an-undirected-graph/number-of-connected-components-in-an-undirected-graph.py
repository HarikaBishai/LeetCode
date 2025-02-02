 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {u: [] for u in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node):
            
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        components = 0
        for i in range(n):
            if i not in visited:
                components+=1
                dfs(i)
        return components
        