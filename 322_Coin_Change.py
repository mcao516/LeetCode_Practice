class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        F[i] = F[i-c] for every coin
        
        """
        F = [0] * (amount + 1)
        
        for a in range(1, amount + 1):
            cuttable = [1e5]
            for c in coins:
                if a >= c:
                    cuttable.append(F[a-c])
            F[a] = min(cuttable) + 1
        
        if F[amount] >= 1e5:
            return -1
        return F[amount]