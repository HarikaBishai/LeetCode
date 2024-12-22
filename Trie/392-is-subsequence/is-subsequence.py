class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len > t_len:
            return False
        if s_len == 0:
            return True
        

        s_p = 0
        t_p = 0

        while s_p < s_len and t_p < t_len:
            if s[s_p] == t[t_p]:
                s_p+=1
                t_p+=1
                if s_p == s_len:
                    return True
            else:
                t_p+=1
        return False