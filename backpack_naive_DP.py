# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # K(n, m) = max(K(n - 1, m), K(n - 1, m - A[n]) + A[n])
        n = len(A)
        K = [[0] * (m + 1) for _ in range(n + 1)]  # [number of item, weight]
        
        for i in range(n + 1):
            for w in range(m + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif A[i-1] > w:
                    K[i][w] = K[i-1][w]
                else:
                    K[i][w] = max(K[i-1][w], K[i-1][w - A[i-1]] + A[i-1])
                    
        return K[n][m]

print(Solution().backPack(10, [3,4,8,5]))