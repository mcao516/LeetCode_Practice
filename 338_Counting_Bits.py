class Solution:
    def countBits(self, num: int) -> List[int]:
        """
        Nums: 0, 1, 2, 3, 4, 5, ...
        Bits: 0, 1, 1, 2, 1, 2, ...
        
        f[i] = f[i // 2] + i % 2
        
        """
        F = [0] * (num + 1)
        for i in range(1, num + 1):
            F[i] = F[i // 2] + (i % 2)
        return F