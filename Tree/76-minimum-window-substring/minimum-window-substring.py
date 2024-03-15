from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = 0

        counter_t = Counter(t)
        counter_s = defaultdict(int)
        l = 0
        min_length = float('inf')
        target_set = set()
        target_l, target_r = -1, -1

        for r in range(len(s)):
            if s[r] in counter_t:
                counter_s[s[r]]+=1
                if counter_s[s[r]] >= counter_t[s[r]] and s[r] not in target_set:
                    target_set.add(s[r])
            
            while len(target_set) == len(counter_t):
                if min_length > r-l+1:
                    min_length = r-l+1
                    target_l = l
                    target_r = r
                if s[l] in counter_t:
                    counter_s[s[l]]-=1
                    if counter_s[s[l]] < counter_t[s[l]]:
                       target_set.remove(s[l])
                l+=1
        return s[target_l: target_r+1] if  min_length!= float('inf') else ""