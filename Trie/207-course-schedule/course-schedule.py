class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = {i: 0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}

        for v, u in prerequisites:
            graph[u].append(v)

            indegree[v]+=1
        visited = set()
        q = deque()
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)
                visited.add(node)


        print(q, visited)
        while q and numCourses:
            node = q.popleft()

            
            numCourses -= 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    visited.add(nei)
        print(numCourses)
        return True if numCourses == 0 else False


