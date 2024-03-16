class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        out = 0
        def getExpressiveWordsMapping(word):
            mapper = []
            for i in range(len(word)):
                if mapper and  mapper[-1][0] == word[i]:
                    mapper[-1][1]+=1
                else:
                    mapper.append([word[i], 1])
            return mapper

        s_mapping = getExpressiveWordsMapping(s)


        for word in words:
            word_mapper = getExpressiveWordsMapping(word)
            if (len(word_mapper) != len(s_mapping)) or len(word_mapper) == 1:
                continue

            i = 0
            while i<len(word_mapper):
                word_count = word_mapper[i]
                s_word_count = s_mapping[i]
                if word_count[0] == s_word_count[0] and word_count[1] <= s_word_count[1] and (word_count[1] == s_word_count[1] or s_word_count[1] >= 3):
                    i+=1
                else:
                    break
            if i == len(word_mapper):
                out+=1

        return out

