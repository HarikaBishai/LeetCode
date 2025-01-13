class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}

        indegree = {i:0 for i in range(numCourses)}
        

        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v]+=1

        
        q = deque()
        finish = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                

        out = []
        
        while q:
            node = q.popleft()
            finish+=1
            out.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
                
        
        return out if finish == numCourses else []






        

        visit = set()
        path = set()

        out = []

        def dfs(i):
            
            visit.add(i)
            path.add(i)
            for nei in graph[i]:
                if nei not in visit:
                    if dfs(nei):
                        return True
                elif nei in path:
                    return True

            path.remove(i)
            out.append(i)
            return False
        

        for v in range(numCourses):
            if v not in visit and dfs(v):
                return []
        
        return out[::-1]