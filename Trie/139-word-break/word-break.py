class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_words(self, words):
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.end_of_word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        trie = Trie()
        trie.add_words(wordDict)
        root = trie.root

        n = len(s)

        dp = [False]* (n)
        
        for i in range(n):
            if i == 0 or dp[i-1]:
                curr = root
                for j in range(i, n):
                    
                    if s[j] not in curr.children:
                        break
                    curr = curr.children[s[j]]
                    if curr.end_of_word:
                        dp[j] = True

                   
        return dp[n-1]


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