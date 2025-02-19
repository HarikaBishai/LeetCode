class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        


        k -= 1

        numbers = [str(i) for i in range(1, n+1)]

        permutation = []

        factorial = math.factorial(n-1)
        for i in range(n-1, -1 , -1):
            if i == 0:
                permutation.append(numbers.pop())
            
            else:

                index = k//factorial

                permutation.append(numbers.pop(index))

                k = k % factorial

                factorial = factorial//i
        return "".join(permutation)
