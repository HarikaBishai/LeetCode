class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        out = []
        stk = []
        words_set = set(wordDict) 
        def dfs(i):
            if i == len(s):
                out.append(" ".join(stk.copy()))
                
                return
            
            for word in wordDict:
                if i + len(word) -1 < len(s) and s[i: i + len(word)] == word:
                    stk.append(word)
                    dfs(i + len(word))
                    stk.pop()
            return
        dfs(0)
        return out
                

            