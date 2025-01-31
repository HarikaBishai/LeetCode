class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        

        wordDict = set(words)
        out = []
     

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