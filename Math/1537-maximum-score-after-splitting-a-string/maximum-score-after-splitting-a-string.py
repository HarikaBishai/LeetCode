class Solution:
    def maxScore(self, s: str) -> int:
        if not s:
            return 0
        left_zeros = [0] * len(s)
        right_ones = [0] * len(s)

        
        for i in range(1, len(s)):
            if s[i-1] == '0':
                left_zeros[i] = left_zeros[i-1] + 1
            else:
                left_zeros[i]  = left_zeros[i-1]
        

        for i in range(len(s)-2, -1, -1):
            if s[i+1] == '1':
                right_ones[i] = right_ones[i+1] + 1
            else:
                right_ones[i] = right_ones[i+1]

        
        left_zeros = left_zeros[1:]
        right_ones = right_ones[:-1]
        
        out = 0
        for i in range(len(s)-1):
            if out < left_zeros[i] + right_ones[i]:
                out = left_zeros[i] + right_ones[i]
        
        return out
