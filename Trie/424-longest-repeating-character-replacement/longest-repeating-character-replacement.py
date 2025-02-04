class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        maxLen = 0
        l = 0
        for i in range(len(s)):
            counter[s[i]]+=1

            while (i-l+1) - max(counter.values())  > k:
                counter[s[l]]-=1
                l+=1
            maxLen = max(maxLen, i-l+1)
        return maxLen
