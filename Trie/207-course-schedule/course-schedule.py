class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # using khan's algo for topology sort

        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v]+=1

        q = deque()
        finish = 0
        for i,val in enumerate(indegree):
            if val == 0:
                q.append(i)


        while q:
            node = q.popleft()
            finish+=1
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)

        return True if finish == numCourses else False
        
        


        # using dfs graph cycle detection
        
        graph = {i: [] for i in range(numCourses)}

        for v, u in prerequisites:
            graph[u].append(v)



        path = set()
        visited = set()

        def dfs(i):

            visited.add(i)
            path.add(i)

            for nei in graph[i]:
                if nei not in visited:
                    if not dfs(nei):
                        return False
                elif nei in path:
                    return False
            path.remove(i)
            return True

        for i in range(numCourses):
            if i not in visited and not dfs(i):
                return False
        return True