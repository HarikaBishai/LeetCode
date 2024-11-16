class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root =  TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(i, root) :
            if i == len(word):
                return True if root.endOfWord else False
            
            curr = root

            c = word[i]

            if c == '.':
                for child in root.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            else:
                if c not in root.children:
                    return False
                else:
                    return dfs(i+1, root.children[c])
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)