class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        q = deque([0])


        wordDict = set(wordDict)
        seen = set([0])

        while q:
            for _ in range(len(q)):
                start = q.popleft()

                if start == len(s):
                    return True


                for word in wordDict:
                    if start+len(word)<= len(s) and  s[start: start+len(word)] in wordDict and start+len(word) not in seen:
                        q.append(start+len(word))
                        seen.add(start+len(word))
                # for end in range(start, len(s)):
                #     if s[start: end+1] in wordDict and end+1 not in seen:
                #         q.append(end+1)
                #         seen.add(end+1)

        return False

