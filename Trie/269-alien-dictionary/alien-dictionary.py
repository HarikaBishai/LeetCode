class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        graph = {c:set() for word in words for c in word }


        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            minLength = min(len(w1), len(w2))

            if w1[:minLength] == w2[:minLength] and len(w1) > len(w2):
                return ""

            for j in range(minLength):
                if w1[j]!=w2[j]:
                    graph[w1[j]].add(w2[j])
                    break

        visited = set()
        path = set()
        res = []

        def dfs(i):
            visited.add(i)
            path.add(i)

            for nei in graph[i]:
                if nei not in visited and dfs(nei):
                    return True
                elif nei in path:
                    return True
            path.remove(i)
            res.append(i)
            return False
        for c in graph.keys():
            if c not in visited:
               if dfs(c):
                return ""
        return "".join(res[::-1])

                
        