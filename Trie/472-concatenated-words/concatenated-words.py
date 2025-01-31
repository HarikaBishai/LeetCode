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


        wordDict = set(words)
        out = []
        minLen = len(words[0])

        for word in words:
            if len(word) < minLen:
                minLen = len(word)

        for word in words:

            dp = [False]*(len(word)+1)
            dp[0]= True
            

            for i in range(1, len(word)+1):
                for j in range(i):
                    if dp[j] and word[j:i] in wordDict and word[j:i] != word:
                        dp[i] = True
                        break
            if dp[-1]:
                out.append(word)

        return out