class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)
        if len(s)!=len(t):
            return False

        count_s = Counter(s)
        count_t = Counter(t)

        if len(count_s) != len(count_t):
            return False
        

        for key, val in count_s.items():
            if key not in count_t:
                return False
            if count_s[key]!=count_t[key]:
                return False
        return True