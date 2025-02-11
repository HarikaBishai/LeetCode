class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*(n) for _ in range(n) ]


        maxLen = 0
        index = 0
        for i in range(n):
            for j in range(i+1):
                if (i - j <=2  or dp[i-1][j+1]) and  s[i] == s[j]:
                    dp[i][j] = True
                    if i-j+1  >= maxLen:
                        maxLen = i-j+1
                        index = j
        print(maxLen, index)
        return s[index: index+maxLen]