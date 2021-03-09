import math

class Solution:
    def numSquares(self, n: int) -> int:
        """
        F[i] = min(F[i-j]) + 1, for every j
        
        """
        m = int(math.sqrt(n))
        squares = [i ** 2 for i in range(1, m + 1)]
        
        F = [0] * (n + 1)
        
        for i in range(1, n + 1):
            cands = []
            for s in squares:
                if s <= i:
                    cands.append(F[i-s] + 1)
            F[i] = min(cands)
        
        return F[n]
        
        