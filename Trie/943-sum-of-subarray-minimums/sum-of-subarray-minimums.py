class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7

        res = 0

        stk = []

        for i, num in enumerate(arr):
            while stk and stk[-1][1] > num:
                idx, val = stk.pop()
                left = idx - stk[-1][0] if stk else idx+1
                right = i - idx
                res =  (res + val * left * right) % MOD
            stk.append((i,num))

        
        for i in range(len(stk)):
            idx, num = stk[i]
            left = idx - stk[i-1][0] if i > 0 else idx+1
            right = len(arr) - idx
            res =  (res + num * left * right) % MOD 

        return res