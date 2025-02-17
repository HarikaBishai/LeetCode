class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) -1
        j = len(num2) -1
        carry = 0
        sum = 0
        out = ""

        while i >= 0 or j >=0 or carry:
            
            sum = carry
            if i>= 0:
                sum+= int(num1[i])
                i-=1
            if j>=0:
                sum+= int(num2[j])
                j-=1
            
            if sum > 9:
                carry = int(sum/10)
                
            else:
                carry = 0
            
            out = str(sum % 10) + out
            sum = 0
            

        return out
                