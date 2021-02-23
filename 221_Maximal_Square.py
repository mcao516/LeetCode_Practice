class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        F(i, j, l) = matrix(i, j) and F(i+1, j, l-1) and F(i, j+1, l-1) and F(i+1, j+1, l-1)
        
        """
        m, n = len(matrix), len(matrix[0])
        max_size = min(m, n)
        F = [[[False] * max_size for _ in range(n)] for _ in range(m)]  # [m, n, max_size]
        
        max_length = 0
        for l in range(max_size):
            for row in range(m-l):
                for col in range(n-l):
                    if l == 0:
                        F[row][col][l] = matrix[row][col] == "1"
                    else:
                        F[row][col][l] = F[row][col][0] and F[row+1][col][l-1] and F[row][col+1][l-1] and F[row+1][col+1][l-1]
                        
                    if F[row][col][l] and (l + 1) > max_length:
                        max_length = l + 1
        
        return max_length * max_length