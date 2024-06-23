class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph  = {i:[] for i in range(numCourses)}

        for dest, src in prerequisites:
            graph[src].append(dest)

        visited = set()
        path = set()
        out = []
        
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
            out.append(i)
            return False
        
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return []
        
        return out[::-1]
