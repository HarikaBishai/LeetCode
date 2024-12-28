class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return "" 
        minLen = len(s) + 1
        count_t = Counter(t)
        have = 0
        need = len(count_t)
        counter_s = {}

        l = 0
        min_l = -1
        for r in range(len(s)):
            counter_s[s[r]] = 1 + counter_s.get(s[r], 0)

           
            if s[r] in count_t and counter_s[s[r]] == count_t[s[r]]:
                have+=1
            while have == need:
                if r-l+1 < minLen:
                    minLen = r-l+1
                    min_l = l
                counter_s[s[l]] -= 1
                if s[l] in count_t and counter_s[s[l]] < count_t[s[l]]:
                    have-=1
                l+=1
        return s[min_l: min_l+minLen] if min_l >= 0 else ""
                

