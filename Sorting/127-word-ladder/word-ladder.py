class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' +word[j+1:]
                graph[pattern].append(word)

        print(graph)

        res = 1


        def bfs():
            visited = set([beginWord])
            q = deque([beginWord])
            res = 1
            while q:

                for i in range(len(q)):
                    word = q.popleft()

                    if word == endWord:
                        return res
                    
                    for j in range(len(word)):
                        pattern =  word[:j] + '*' +word[j+1:]
                        for nei in graph[pattern]:
                            if nei not in visited:
                                q.append(nei)
                                visited.add(nei)
                res+=1 

            return 0
        res = bfs()
        return res