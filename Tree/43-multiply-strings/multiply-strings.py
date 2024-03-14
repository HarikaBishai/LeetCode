class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        multiplier = 1
        total = 0
        for i in range(len(num2)-1, -1, -1):
            curr = int(num2[i])

            curr_sum = 0
            carry  = 0
            curr_multiplier = 1
            for j in range(len(num1)-1, -1, -1):
                
                prod = curr*(ord(num1[j])- ord('0')) + carry
                curr_sum += (prod%10)*curr_multiplier 
                carry = prod //10
                curr_multiplier *= 10

            if carry:
                curr_sum = carry * curr_multiplier + curr_sum
            total += curr_sum*multiplier
            multiplier *= 10

        return str(total) 

            