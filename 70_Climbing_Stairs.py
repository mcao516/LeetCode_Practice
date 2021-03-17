class Solution:
    K = {1: 1, 2: 2}
    
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        elif n == 2: return 2
        else:
            if n - 1 not in self.K:
                self.K[n-1] = self.climbStairs(n-1)
            return self.K[n-1] + self.K[n-2]


class Solution2:
    def climbStairs(self, n: int) -> int:
        """
        F[i] = F[i-1] + F[i-2]
        
        """
        F = [1] * (n + 1)
        
        for i in range(2, n + 1):
            F[i] = F[i-1] + F[i-2]
        
        return F[n]