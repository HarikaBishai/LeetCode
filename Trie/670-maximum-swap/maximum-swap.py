class Solution:
    def maximumSwap(self, num: int) -> int:
        
        
        digits_int = list(str(num))
        n = len(digits_int)
        max_right_index = [0]*n
        max_right_index[n-1] = n-1
        
        for i in range(len(digits_int)-2, -1, -1):
            max_right_index[i] = i if digits_int[i] > digits_int[max_right_index[i+1]] else max_right_index[i+1]
        
        

        for i in range(n):
            if digits_int[i] < digits_int[max_right_index[i]]:
                digits_int[i],  digits_int[max_right_index[i]] =  digits_int[max_right_index[i]], digits_int[i]
                break

        return int("".join(digits_int))


