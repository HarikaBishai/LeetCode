class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        

        graph = defaultdict(list)


        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set([0])

        def dfs(node):
            curr_time = 0
            
            for nei in graph[node]:
                
                if nei not in visited:
                    visited.add(nei)
                    childtime = dfs(nei)
                    if childtime > 0 or hasApple[nei]:
                        curr_time += 2 + childtime
                    
            return curr_time


        
        return dfs(0)