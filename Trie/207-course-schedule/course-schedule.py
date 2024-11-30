class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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