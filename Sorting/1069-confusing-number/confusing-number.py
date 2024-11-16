class Solution:
    def confusingNumber(self, n: int) -> bool:
        if not n: return False
        rotations= {
            0:0,
            1:1,
            6:9,
            8:8,
            9:6
        }
        rev = 0
        temp = n
        while temp:
            curr = temp % 10
            if curr not in rotations:
                return False
            
            rev = rev * 10 + rotations[curr] % 10
            temp = temp // 10
       

        return True if n!=rev else False 
            
