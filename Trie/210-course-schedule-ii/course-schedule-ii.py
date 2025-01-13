class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}



        for v, u in prerequisites:
            graph[u].append(v)

        

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