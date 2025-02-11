class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        out = []
        def dfs(i,stk):
            if i == len(s):
                out.append(" ".join(stk))
                return
            
            for word in wordDict:
                if i+len(word) <= len(s) and s[i: i+len(word)] == word:
                    stk.append(word)
                    dfs(i+len(word), stk)
                    stk.pop()
            return
        dfs(0, [])
        return out