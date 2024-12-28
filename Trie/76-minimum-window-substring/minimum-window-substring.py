class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return "" 
        minLen = len(s) + 1
        count_t = Counter(t)
        target = set()
        counter_s = {}

        l = 0
        min_l = -1
        for r in range(len(s)):
            counter_s[s[r]] = 1 + counter_s.get(s[r], 0)

           
            if s[r] in count_t and counter_s[s[r]] == count_t[s[r]] and s[r] not in target:
                target.add(s[r])
            while len(target) == len(count_t):
                if r-l+1 < minLen:
                    minLen = min(r-l+1, minLen)
                    min_l = l
                counter_s[s[l]] -= 1
                if counter_s[s[l]] < count_t[s[l]]:
                    target.remove(s[l])
                l+=1
        return s[min_l: min_l+minLen] if min_l >= 0 else ""
                

