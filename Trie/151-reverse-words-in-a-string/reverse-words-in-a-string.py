class Solution:
    def reverseWords(self, s: str) -> str:
        s= reversed(list(filter(lambda x: len(x) > 0, s.strip(' ').split(" "))))
        return " ".join(s)

