class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(numCourses)}

        for dest, src in prerequisites:
            graph[src].append(dest)
          
        
        visited = set()
        path = set()
        def dfs(i):
            visited.add(i)
            path.add(i)

            for nei in graph[i]:
                if nei not in visited:
                    if dfs(nei):
                        return True
                elif nei in path:
                    return True

            path.remove(i)
            return False


        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False

        return True
        