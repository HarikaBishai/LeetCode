class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_comb_list = []
        mapping = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}


        # stk = []
        # out = []
        # def dfs(i, stk):
        #     if i == len(digits):
        #         if stk:
        #             out.append("".join(stk))
        #         return
        #     for c in mapping[digits[i]]:
        #         stk.append(c)
        #         dfs(i+1, stk)
        #         stk.pop()

        # dfs(0, stk)
        # return out




        # dp = {"":[]}

        # def backtrack(numstring):
        #     if numstring in dp:
        #         return dp[numstring]

        #     curr_letters = list(mapping[numstring[0]])
        #     for i in range(1, len(numstring)):
        #         remaining_str = numstring[i:]
        #         out = []
        #         sub_str = backtrack(remaining_str)
        #         for sub in sub_str:
        #             for curr in curr_letters:
        #                 out.append(curr+sub)
        #         curr_letters = out
        #     dp[numstring] = curr_letters
        #     return curr_letters

        # return backtrack(digits)
         



        def backtrack(numstring, comb_string):
            if not numstring:
                return
            nonlocal letter_comb_list
            num = numstring[0]
            string = mapping[num]

            for i in string:
                if len(numstring) > 1:
                    backtrack(numstring[1:],comb_string+i)
                else:
                    letter_comb_list.append(comb_string+i)

        backtrack(digits, "")
        return letter_comb_list

            

        