class Solution:
    DP = {0: 1, 1: 1, 2: 2}
    
    def numTrees(self, n: int) -> int:
        if n in self.DP: return self.DP[n]
        else:
            total = 0
            for left in range(n):
                right = n - 1 - left
                total += self.numTrees(left) * self.numTrees(right)
    
            self.DP[n] = total
            return self.DP[n]


class Solution2:
    def numTrees(self, n: int) -> int:
        F = [0] * (n + 1)
        F[0], F[1] = 1, 1
        
        for i in range(2, n + 1):
            for j in range(i):
                F[i] += F[j] * F[i - 1 - j]
        
        return F[n]