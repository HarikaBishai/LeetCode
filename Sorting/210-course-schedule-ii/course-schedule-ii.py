class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c:[] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            graph[crs].append(pre)
            
        visited, cycle = set(), set()
        output = []
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in graph[crs]:
                if dfs(pre) == False:
                    return False
            visited.add(crs)
            cycle.remove(crs)
            output.append(crs)
            
            return True
        
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
        
            
        
        
        
        
        