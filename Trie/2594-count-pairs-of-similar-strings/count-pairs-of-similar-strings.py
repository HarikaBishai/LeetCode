class Solution:
    def similarPairs(self, words: List[str]) -> int:
        seen = {}

        out = 0
        for word in words:
            s_word = "".join(sorted(list(set(word))))
            if s_word in seen:
                seen[s_word]+=1
                out += (seen[s_word]-1)
                
            else:
                seen[s_word] = 1

       
            
        return out
