class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        left = 0
        right = len(s)-1

        s = list(s)
        moves = 0

        while left < right:
            l = left
            r = right

            while l < r and s[l]!=s[r]:
                l+=1

            if l == r:
                s[l-1], s[l] = s[l], s[l-1]
                moves+=1
                continue
            
            for i in range(l, left, -1):
                s[i], s[i-1] = s[i-1], s[i]
                moves+=1
            
            left+=1
            right-=1

        return moves