class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        word_set = set(wordDict)

        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j: i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


        # def dfs(i):
        #     if i == len(s):
        #         return True
            
        #     for word in wordDict:
        #         if i+len(word) <= len(s) and s[i: i+len(word)] in word_set:
        #             if dfs(i+len(word)):
        #                 return True
        #     return False
        # return dfs(0)
