class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = [beginWord] + wordList

        graph = defaultdict(list)


        for word in wordList:
            for i in range(len(word)):
                reg = word[:i] + '*' + word[i+1:]
                graph[reg].append(word)

        q = deque([beginWord])

        visited = set([beginWord])
        count = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    reg = word[:i] + '*' + word[i+1:]
                    for nei in graph[reg]:
                        if nei not in visited:

                            q.append(nei)
                            visited.add(nei)
            count+=1

        return 0