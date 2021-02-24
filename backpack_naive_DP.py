# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        """
        F(n, m) = max(F(n - 1, m), F(n - 1, m - A[n]) + A[n])

        """
        n = len(A)
        F = [[0] * (m + 1) for _ in range(n + 1)]  # [number of item, weight]
        
        for i in range(1, n + 1):  # item
            for w in range(1, m + 1):  # left weight
                F[i][w] = F[i-1][w]
                if w >= A[i-1]:
                    F[i][w] = max(F[i-1][w], F[i-1][w - A[i-1]] + A[i-1])
                    
        return F[n][m]

print(Solution().backPack(10, [3,4,8,5]))