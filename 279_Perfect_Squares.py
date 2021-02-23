import math

class Solution:
    def numSquares(self, n: int) -> int:
        """
        F(j) = min(F(j - cand[i]) for every possible i) + 1
        
        """
        candidates = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
        F = [0] * (n + 1)
        
        for i in range(1, n + 1):
            nums = []
            for c in candidates:
                if i >= c:
                    nums.append(F[i - c] + 1)
            F[i] = min(nums)

        return F[n]
                    
        