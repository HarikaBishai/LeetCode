class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        i = 0
        
        valid_mapping = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        
        while i<len(s):
            if s[i] in ['(', '{', '['] :
                stk.append(s[i])
            else:
                if not stk or stk.pop() != valid_mapping[s[i]]:
                    return False
            i+=1
        if stk:
            return False
        
        return True