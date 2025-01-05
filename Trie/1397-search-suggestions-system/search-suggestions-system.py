class TrieNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.endOfWord = False
        self.strings = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        start = TrieNode("")
        for product in products:
            curr = start
            for char in product:
                if char not  in curr.children:
                    curr.children[char] =  TrieNode(char)
                curr = curr.children[char]
                if len(curr.strings)<3:
                    curr.strings.append(product)
            curr.endOfWord == True

        out = []
        curr = start
        i = 0
        while i < len(searchWord):
            char = searchWord[i]
            if char in curr.children:
                curr = curr.children[char]
                out.append(curr.strings)
            else:
                break
            i+=1

        while i < len(searchWord):
            out.append([])
            i+=1
                
        return out
                

