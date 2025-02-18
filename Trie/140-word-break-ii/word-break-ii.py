class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        out = []
        stk = []

        memo = {"": [""]}
        words_set = set(wordDict)

        def dfs(remaining_str):
            
            if remaining_str in memo:
                return memo[remaining_str]
          
            sentences = []

            for i in range(1, len(remaining_str)+1):
                
                    
                curr_word = remaining_str[:i]
                if curr_word in words_set:
                    sub_setences =  dfs(remaining_str[i:])
                    for sub in sub_setences:
                        if sub:
                            sentences.append(curr_word + " " + sub)
                        else:
                            sentences.append(curr_word)
            memo[remaining_str] = sentences

            return  memo[remaining_str]
        dfs(s)

        return memo[s]




        def dfs(i):
            if i in memo:
                return memo[i]
            sentences = []
            for word in wordDict:
                if i + len(word) -1 < len(s) and s[i: i + len(word)] == word:
                    sub_sentence = dfs(i + len(word))
                    sentences+= sub_sentence

        def dfs(i):
            if i == len(s):
                out.append(" ".join(stk.copy()))
                
                return
            
            for word in wordDict:
                if i + len(word) -1 < len(s) and s[i: i + len(word)] == word:
                    stk.append(word)
                    dfs(i + len(word))
                    stk.pop()
            return
        dfs(0)
        return out
                

            