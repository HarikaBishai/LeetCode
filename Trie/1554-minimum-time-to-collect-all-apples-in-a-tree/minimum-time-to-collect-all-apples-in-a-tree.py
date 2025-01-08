class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {i:[] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(curr, par):

            time = 0

            for child in graph[curr]:
                if child == par:
                    continue
                
                childtime = dfs(child,curr) 
                if childtime or hasApple[child]:
                    time += 2 + childtime 
            return time
        
        return dfs(0, -1)


    