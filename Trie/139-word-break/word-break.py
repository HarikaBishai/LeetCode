class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False]*len(s)

        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) -1:
                    continue
                
                if (i == len(word) - 1 or dp[i-len(word)]) and s[i-len(word)+1: i+1] == word:
                    dp[i] = True
                    break
        
        return dp[-1]