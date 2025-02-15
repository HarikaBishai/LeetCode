class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        



        def check_match(m, n):
            if n == 0:
                return m == 0

            if m == 0:
                return (n >= 2 and p[n-1] == '*') and check_match(m, n-2)
            

            if s[m-1] == p[n-1] or p[n-1] == '.':
                return check_match(m-1, n-1)
            
            if p[n-1] == '*' and n > 1:

                zero_match = check_match(m, n-2)
                one_or_more_match = (s[m-1] == p[n-2] or p[n-2] == '.') and check_match(m-1, n)
                return zero_match or one_or_more_match
            return False

        return check_match(len(s), len(p))