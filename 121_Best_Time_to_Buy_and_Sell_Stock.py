class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        F[i] = max(prices[i] - prices[i-1], prices[i] - prices[i-1] + F[i-1])
        
        """
        n = len(prices)
        F = [0] * n
        
        F[0] = 0
        for i in range(1, n):
            if F[i - 1] > 0:
                F[i] = prices[i] - prices[i-1] + F[i-1]
            else:
                F[i] = prices[i] - prices[i-1]
                
        return max(F)


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # K(i) = (K(i+1) > 0 ? K(i+1) : 0) + A[i+1] - A[i]
        # K(i) = (K(i-1) > 0 ? K(i-1) : 0) + A[i] - A[i-1]
        n = len(prices)
        F = [0] * n
        
        if n == 1: return 0
        
        F[0] = 0
        F[1] = prices[1] - prices[0]
        max_profit = F[1]
        
        for i in range(2, n):
            if F[i-1] > 0:
                F[i] = F[i-1] + prices[i] - prices[i-1]
            else:
                F[i] = prices[i] - prices[i-1]
                
            if F[i] > max_profit: max_profit = F[i]
                
        return max(0, max_profit)