class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self, dictionary):
        self.root = TrieNode()
        for word in dictionary:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endOfWord = True
        
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        root = Trie(dictionary).root
        dp = {len(s): 0}

        def dfs(i):

            if i in dp:
                return dp[i]

            res = 1+ dfs(i+1)

            curr = root
            for j in range(i, len(s)):
                c = s[j]
                if c not in curr.children:
                    break
                curr = curr.children[c]
                if curr.endOfWord:
                    res = min(res, dfs(j+1))
                    
            dp[i] = res
            return res
        
        return dfs(0)
        