class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i: 0 for i in range(numCourses)}

        graph = {i:[] for i in range(numCourses)}


        out = []

        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v]+=1

        q = deque()
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)
        


        while q:
            node = q.popleft()

            out.append(node)

            for nei in graph[node]:
                indegree[nei]-=1

                if indegree[nei] == 0:
                    q.append(nei)

        

        return out if len(out) == numCourses else []