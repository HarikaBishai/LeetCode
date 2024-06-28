class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        hash = [0]*26
        maxlen = 0
        for r in range(len(s)):
            hash[ord('A')-ord(s[r])]+=1

            while (r-l+1) - max(hash) > k:
                hash[ord('A')-ord(s[l])]-=1
                l+=1
            maxlen = max(maxlen, r-l+1)

        return maxlen