class Solution:
    def decodeString(self, s: str) -> str:
        stk = []

        i = 0
       
        while i <len(s):
            if s[i] == ']':
                curr_s = ''
                while stk and  stk[-1]!='[':
                    curr_s = stk.pop() + curr_s
                
                stk.pop()

                curr_num = ''
                while stk and stk[-1].isdigit():
                    curr_num = stk.pop() + curr_num
                
                stk.append(curr_s * int(curr_num))

            else:
                stk.append(s[i])
            i+=1
           

        return "".join(stk)
        

