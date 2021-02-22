class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        F(row, col) = F(row + 1, col) + F(row, col + 1)
        
        """
        F = [[0] * n for _ in range(m)]  # [m, n]
        
        F[m-1][n-1] = 1
        for row in reversed(range(m)):
            for col in reversed(range(n)):
                right_paths, down_paths = 0, 0
                
                if row + 1 < m:
                    down_paths = F[row + 1][col]
                if col + 1 < n:
                    right_paths = F[row][col + 1]
                    
                F[row][col] += down_paths + right_paths
        
        return F[0][0]
        