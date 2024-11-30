class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(n)}


        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)



        visited = set()
        def dfs(i, parent):
            visited.add(i)

            for nei in graph[i]:
                if nei not in visited:
                    if not dfs(nei, i):
                        return False
                elif parent!=nei:
                    return False
            return True
        

        
        if not dfs(0, None):
            return False
        
        
        return False if len(visited)!= n else True


        