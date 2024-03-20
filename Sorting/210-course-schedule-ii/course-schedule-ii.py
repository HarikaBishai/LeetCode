class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for csc, pre in prerequisites:
            graph[csc].append(pre)

        visited , cycle = set(), set()
        out = []

        def dfs(crc):
            if crc in cycle:
                return False
            if crc in visited:
                return True

            visited.add(crc)
            cycle.add(crc)
            
            for pre in graph[crc]:
                if dfs(pre) == False:
                    return False
            
            out.append(crc)
            cycle.remove(crc)

        for i in range(numCourses):
            if i not in visited:
                if dfs(i) == False:
                    return []
        return out