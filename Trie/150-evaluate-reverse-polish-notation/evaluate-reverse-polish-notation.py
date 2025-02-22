class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        out = 0

        operations = set(["*", "/", "+", "-"])

        stk = []

        for token in tokens:
            if token in operations:
                if token == '*':
                    stk.append(int(stk.pop())* int(stk.pop()))
                elif token == '/':
                    a = int(stk.pop())
                    b = int(stk.pop())
                    stk.append(int(b / a))
                elif token == '+':
                    a = int(stk.pop())
                    b = int(stk.pop())
                    stk.append(b + a)
                else:
                    a = int(stk.pop())
                    b = int(stk.pop())
                    stk.append(b - a)
            
            else:
                stk.append(token)
           
        return int(stk[0])