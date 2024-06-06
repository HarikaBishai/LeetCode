import re
class Solution:


    def isValid(self, code: str) -> bool:

        def isValidTagName(tagName):
            pattern = r'^[A-Z]{1,9}$'
            return re.match(pattern,tagName)

        def validateCode(code):
            i = 0
            stack = []

            while i<len(code):
                if i > 0 and not stack:
                    return False
                if code[i:i+9] == "<![CDATA[":
                    j = i+9
                    i = code.find(']]>', j)
                    if i==-1:
                        return False
                    i = i+3
                elif code[i:i+2] == '</':
                    j = i+2
                    i = code.find('>', j)

                    if i==-1:
                        return False
                    tagname = code[j:i]
                    if not stack or  stack[-1] != tagname:
                        return False
                    stack.pop()
                    i=i+1
                elif code[i] == '<':
                    j=i+1
                    i = code.find('>', j)

                    if i == -1:
                        return False
                    tagname = code[j:i]
                    print(tagname)
                    if not isValidTagName(tagname):
                        return False
                    stack.append(tagname)
                    i=i+1
                else:
                    i+=1
            return not stack
        return validateCode(code)

        