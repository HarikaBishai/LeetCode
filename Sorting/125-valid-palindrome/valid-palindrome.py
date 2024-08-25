class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]','', s.lower())
        return True if s[::-1] == s else False
        