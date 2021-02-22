class Solution:
    K = {1: 1, 2: 2}
    
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        elif n == 2: return 2
        else:
            if n - 1 not in self.K:
                self.K[n-1] = self.climbStairs(n-1)
            return self.K[n-1] + self.K[n-2]