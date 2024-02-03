class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        if n == 1 and k == 1:
            return 1
        first_factors = []
        last_factors = []
        i = 1
        
        while i <= n ** 0.5 and len(first_factors) < k:
            if n%i == 0:
                first_factors.append(i)
                if n//i not in first_factors:
                    last_factors.append(n//i)
            i += 1

        if len(first_factors) >= k:
            return first_factors[k-1]
        elif len(first_factors) + len(last_factors) >= k :
            return last_factors[len(last_factors) - (k-len(first_factors)-1) -1]
        else:
            return -1