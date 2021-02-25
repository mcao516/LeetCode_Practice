class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        F(i, j) = F(i-1, j) + F(i-1, j - nums[j])
        
        """
        n, m = len(nums), sum(nums) + S
        
        if m % 2 == 1:
            return 0
        elif sum(nums) < S:
            return 0
        
        m = m // 2
        F = [[None] * (m + 1) for _ in range(n + 1)]  # [n+1, m+1]
        
#         for i in range(n+1):  # no value left  
#             F[i][0] = 1
            
        for i in range(1, m + 1):  # no number left
            F[0][i] = 0
        
        F[0][0] = 1
        for i in range(1, n+1):  # number
            for j in range(0, m+1):  # left value
                if j >= nums[i-1]:
                    F[i][j] = F[i-1][j] + F[i-1][j - nums[i-1]]
                else:
                    F[i][j] = F[i-1][j]
        
        return F[-1][-1]
    

class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        new_nums = []
        for n in nums:
            if n != 0:
                new_nums.append(n)
        
        n, m = len(new_nums), sum(nums) - S
        if m < 0: return 0
        elif m == 0: return 2**nums.count(0)
        
        F = [[0] * (m + 1) for _ in range(n + 1)]  # [n+1, m+1]
        
        for i in range(n+1):  # no value left  
            F[i][0] = 1
            
        for i in range(1, m + 1):  # no number left
            F[0][i] = 0
        
        for i in range(1, n+1):  # number
            for j in range(1, m+1):  # left value
                if j >= 2 * new_nums[i-1]:
                    F[i][j] = F[i-1][j] + F[i-1][j - 2 * new_nums[i-1]]
                else:
                    F[i][j] = F[i-1][j]
        
        return F[-1][-1] * 2**nums.count(0)