class Solution:
    def calculate(self, s: str) -> int:
        stk = []

        operation = '+'
        curr_char = 0

        for i, char in enumerate(s):
          
            if  char.isdigit():
                curr_char = (curr_char * 10 )+ int(char)
            if (char!= " " and (not char.isdigit())) or i==len(s)-1:
                if operation == '+':
                    stk.append(curr_char)
                elif operation == '-':
                    stk.append(-curr_char)
                elif operation == '*':
                    top = stk.pop()
                    stk.append(top * curr_char)
                elif operation == '/':
                    top = stk.pop()
                    stk.append(int(top / curr_char))
                operation = char
                curr_char = 0
        out = 0

        while stk:
            out+= stk.pop()
        return out