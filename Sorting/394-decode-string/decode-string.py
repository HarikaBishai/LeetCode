class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s

        out = ''

        stk = []

        i = 0

        while i < len(s):
            char =  s[i]
            
            if char == ']':

                curr_str = ''
                while stk[-1] != '[':
                    curr_str = stk.pop() + curr_str
                stk.pop()
                
                print(stk)
                curr_num = ''
                while stk and len(stk[-1]) == 1 and ord(stk[-1]) >= ord('0') and ord(stk[-1]) <= ord('9'):
                    curr_num = stk.pop() + curr_num
                stk.append((curr_str*int(curr_num)))
            else:
                stk.append(char)
            i+=1
                
        return ''.join(stk)
        