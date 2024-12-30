class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        arr = [float('-inf')] + arr + [float('-inf')]

        stk = []
        res = 0
        for i, num in enumerate(arr):
            while stk and stk[-1][1] > num:
                j, n = stk.pop()
                left = j - stk[-1][0] if stk else j+1
                right = i-j
                res = (res + n * left * right ) % MOD
        
            stk.append((i,num))
        return res

