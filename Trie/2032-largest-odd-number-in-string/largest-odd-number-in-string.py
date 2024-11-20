class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        first_odd = -1
        i = len(num)-1
        while i >= 0:
            if int(num[i])%2 != 0:
                first_odd = i
                break
            i-=1
        
        return num[:i+1] if first_odd!=-1 else ""