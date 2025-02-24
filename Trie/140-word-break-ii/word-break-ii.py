class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        out = []
        dp = {"": [""]}
        words_set = set(wordDict)

        def dfs(s):
            if s in dp:
                return dp[s]
            sentences = []

            for i in range(1, len(s) +1):
                curr_word = s[:i]
                if curr_word in words_set:
                    sub_sentences = dfs(s[i:])
                    for sub in sub_sentences:
                        if sub:
                            sentences.append(curr_word + " " + sub)
                        else:
                            sentences.append(curr_word)
            dp[s] = sentences
            return dp[s]
        return dfs(s)
