class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_comb_list = []
        mapping = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}


        dp = {"": [""]}

        def dfs(digits):
            if digits in dp:
                return dp[digits]
            first_digit = digits[0]
            remaining_digits = digits[1:]
            remaining_sub = dfs(remaining_digits)
            out = []
            for digit in mapping[first_digit]:
                for sub in remaining_sub:
                    
                    out.append(digit + sub)
                    

            dp[digits] = out
            return out
        out = dfs(digits) 
        return out if out!=[""] else []

        stk = []
        out = []
        def dfs(i, stk):
            if i == len(digits):
                if stk:
                    out.append("".join(stk))
                return
            for c in mapping[digits[i]]:
                stk.append(c)
                dfs(i+1, stk)
                stk.pop()

        dfs(0, stk)
        return out




        

            

        