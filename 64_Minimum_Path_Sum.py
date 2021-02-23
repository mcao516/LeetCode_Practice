class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        F(row, col) = min(F(row + 1, col), F(row, col + 1)) + grid[row][col]
        
        """
        row_num, col_num = len(grid), len(grid[0])
        F = [[0] * col_num for _ in range(row_num)]
        
        F[row_num-1][col_num-1] = grid[row_num-1][col_num-1]
        
        for row in reversed(range(row_num)):
            for col in reversed(range(col_num)):
                if row == row_num -1 and col == col_num - 1:
                    continue
                
                down_weight, right_weight = 1e5, 1e5
                
                if row + 1 < row_num:
                    down_weight = F[row+1][col]
                if col + 1 < col_num:
                    right_weight = F[row][col+1]
                
                F[row][col] = min(down_weight, right_weight) + grid[row][col]
                
        return F[0][0]
        