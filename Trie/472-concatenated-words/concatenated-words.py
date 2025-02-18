class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        


        res = []
        words_set = set(words)
        for word in words:
            dp = [False]*(len(word)+1)
            dp[0] = True

            for i in range(1,len(word)+1):
                for j in range(i):
                    curr_word = word[j:i]
                    if dp[j] and curr_word in words_set and curr_word!=word:
                        dp[i] = True
                        break
            if dp[len(word)]:
                res.append(word)
        return res