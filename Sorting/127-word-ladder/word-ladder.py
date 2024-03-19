class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = collections.defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                graph[pattern].append(word)

        print(graph)
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1

        while q:

            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nei in graph[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res+=1
        return 0