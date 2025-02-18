class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.words = []
class Trie:
    def __init__(self):
        self.root = Node()
    def add_words(self, words):
        words.sort()
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node()
                
                
                curr = curr.children[c]
                if len(curr.words) < 3:
                    curr.words.append(word)
                
            curr.end_of_word = True


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        trie.add_words(products)
        root = trie.root

        out = []
        curr = root

        i = 0
        for c in searchWord:
            if c in curr.children:
                curr = curr.children[c]
                out.append(curr.words)
            else:
                break
            i+=1
        while i < len(searchWord):
            out.append([])
            i+=1
        return out