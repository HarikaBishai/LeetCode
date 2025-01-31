class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        def checkConcatenation(wordDict, s):
            dp = [False]*(len(s)+1)
            dp[0]= True
            

            for i in range(1, len(s)+1):
                for j in range(i):
                    if dp[j] and s[j:i] in wordDict and s[j:i] != s:
                        dp[i] = True
                        break
            return dp[-1]


            # q = deque([0])


            # wordDict = set(wordDict)
            # seen = set([0])

            # while q:
            #     for _ in range(len(q)):
            #         start = q.popleft()

            #         if start == len(s):
            #             return True


            #         for word in wordDict:
            #             if start+len(word)<= len(s) and  s[start: start+len(word)] in wordDict and start+len(word) not in seen:
            #                 q.append(start+len(word))
            #                 seen.add(start+len(word))

            # return False

        out = []
        minLen = len(words[0])

        for word in words:
            if len(word) < minLen:
                minLen = len(word)
        for i, word in enumerate(words):

            if len(word) >= minLen * 2 and checkConcatenation(set(words), word):
                out.append(word)
        return out