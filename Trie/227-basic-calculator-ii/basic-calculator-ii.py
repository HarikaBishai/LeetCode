class Solution:
    def calculate(self, s: str) -> int:
        
        stk = []
        


        numbers = set([str(i) for i in range(10)])
        operations = set(["-", "+", "/", "*"])

        curr_num = 0
        operation = '+'
        for i, c in enumerate(s):
            if c in numbers:
                curr_num = curr_num * 10 + int(c)
                
            if c in operations or i == len(s) - 1:
                if operation == '-':
                    stk.append(-curr_num)
                elif operation == '+':
                    stk.append(curr_num)
                elif operation == '/':
                    stk[-1] = int(stk[-1] / curr_num)
                else:
                    stk[-1] = stk[-1] * curr_num
                
                curr_num = 0
                operation = c
        return sum(stk)


