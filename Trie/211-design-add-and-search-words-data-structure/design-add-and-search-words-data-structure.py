class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()


    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr =  curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            if i == len(word):
                return node.endOfWord
            
            if word[i] != '.':
                return word[i] in node.children and dfs(i+1, node.children[word[i]])

            else:
                for child in node.children:
                    if dfs(i+1, node.children[child]):
                        return True
            return False

        return dfs(0, self.root)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)