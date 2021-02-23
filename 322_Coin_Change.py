class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        F(i) = min(F(i - c) for every c) + 1
        
        """
        F = [0] * (amount + 1)
        min_value = min(coins)
        
        F[0] = 0
        for i in range(1, amount + 1):
            nums = []
            if i < min_value:  # no coin can further break
                nums.append(1e5)
            
            for c in coins:
                if i >= c:
                    nums.append(F[i-c])
            F[i] = min(nums) + 1
        
        if F[amount] >= 1e5:
            return -1
        else:
            return F[amount]