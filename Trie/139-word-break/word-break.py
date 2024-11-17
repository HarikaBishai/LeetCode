class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        mem = {}

        def dp(i):
            if i < 0: return True
            if i in mem: return mem[i]
            for word in wordDict:
                if s[i-len(word)+1: i+1] == word and dp(i-len(word)):
                    mem[i] = True
                    return True
            mem[i] = False
            return False
        return dp(len(s)-1)