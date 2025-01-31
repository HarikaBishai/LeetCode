class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)

        dp[0] = True
        wordDict = set(wordDict)

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]




        # q = deque([0])


        # wordDict = set(wordDict)
        # seen = set([0])

        # while q:
        #     for _ in range(len(q)):
        #         start = q.popleft()

        #         if start == len(s):
        #             return True


        #         for word in wordDict:
        #             if start+len(word)<= len(s) and  s[start: start+len(word)] in wordDict and start+len(word) not in seen:
        #                 q.append(start+len(word))
        #                 seen.add(start+len(word))

        # return False

