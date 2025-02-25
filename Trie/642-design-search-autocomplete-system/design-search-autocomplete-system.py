class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)
        
        self.curr_search = []
        self.dead_node = TrieNode()
        self.curr_node = self.root

    
    def add_to_trie(self, sentence, count):
        curr = self.root
        
        for c in sentence:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.sentences[sentence]+= count
        

    def input(self, c: str) -> List[str]:
        if c == '#':
            curr_sentence = "".join(self.curr_search)
            self.add_to_trie(curr_sentence, 1)
            self.curr_node = self.root
            self.curr_search = []
            return []
        
        self.curr_search.append(c)
        if c not in self.curr_node.children:
            self.curr_node = self.dead_node
            return []

        self.curr_node = self.curr_node.children[c]

        sentences = self.curr_node.sentences
        search_sentences = sorted(sentences.items(), key= lambda x:(-x[1], x[0]) )

        ans = []
        for i in range(min(3,len(search_sentences))):
            ans.append(search_sentences[i][0])
        
        return ans

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)