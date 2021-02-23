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