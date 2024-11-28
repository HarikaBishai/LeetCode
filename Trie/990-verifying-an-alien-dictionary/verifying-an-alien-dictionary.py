class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {c:i for i, c in enumerate(order)}


        def dfs(w1, w2, i):
            if i >= len(w1):
                return True
            
            if i >= len(w2):
                return False

            if dictionary[w1[i]] < dictionary[w2[i]]:
                return True
            elif dictionary[w1[i]] > dictionary[w2[i]]:
                return False
            else:
                return dfs(w1, w2, i+1)
            



        for i in range(len(words)-1):
            if not dfs(words[i], words[i+1], 0):
                return False
        
        return True