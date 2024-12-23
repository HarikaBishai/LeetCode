class Solution:
    def maxDepth(self, s: str) -> int:
        balance = 0

        max_length = 0

        for char in s:
            if char == '(':
                balance+=1
            elif char == ')':
                balance-=1
            max_length = max(max_length, balance)
        return max_length