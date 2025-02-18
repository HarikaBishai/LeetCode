class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]
        


        def dfs(i):
            if i == len(s):
                return True
            
            for word in wordDict:
                if i + len(word) -1 < len(s) and s[i: i+len(word)] == word:
                    if dfs(i+len(word)):
                        return True
            

            return False
        
        return dfs(0)