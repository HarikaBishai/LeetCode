class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        out = 0

        l = 0
        for r in range(len(s)):
            count[s[r]]+=1
            while (r-l+1) - max(count.values()) > k and l < len(s):
                count[s[l]]-=1
                if count[s[l]] == 0:
                    del count[s[l]]
                l+=1
            out = max(out, r-l+1)
        return out
