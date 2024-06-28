class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        n = len(s)
        k = len(words)
        wlen = len(words[0])
        win_size = k*wlen
        word_count = Counter(words)

        def check(i):

            copy_count = word_count.copy()
            target = 0

            for j in range(i, i+win_size , wlen):
                sub = s[j:j+wlen]
                if copy_count[sub] > 0:
                    copy_count[sub]-=1
                    target+=1
                else:
                    break
            return target == k
        out = []
        for i in range(0, n-win_size+1):
            if check(i):
                out.append(i)

        return out