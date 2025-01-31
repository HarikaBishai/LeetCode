class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        path = []
        out = []
        def dfs(i):
            if i == len(s):
                out.append(" ".join(path))
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    path.append(word)
                    dfs(i + len(word))
                    path.pop()
            return False

        dfs(0)

        return out
