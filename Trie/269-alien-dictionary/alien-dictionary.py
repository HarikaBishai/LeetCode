class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        if len(words) == 1: return "".join(list(set(words[0])))
        
        graph = defaultdict(list)
        
        
        dictionary = ""
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            dictionary += word1 + word2
            n1 = len(word1)
            n2 = len(word2)
            minLen = min(n1, n2)

            if word1[:minLen] == word2[:minLen] and n1 > n2:
                return ""
            
            for j in range(minLen):
                
                if word1[j]!=word2[j]:
                    graph[word1[j]].append(word2[j])
                    break

        dictionary = set(list(dictionary))
        indegree = { v:0 for v in dictionary}

        for u in graph:
            for v in graph[u]:
                indegree[v]+=1

        q = deque()
        seen = set()
        for u in indegree:
            if indegree[u] == 0:
                q.append(u)
        out = []

        while q:
            c = q.popleft()

            out.append(c)

            for nei in graph[c]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return "".join(out) if len(out) == len(dictionary) else ""




       