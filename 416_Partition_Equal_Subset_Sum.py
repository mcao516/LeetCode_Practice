class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        F(j, i) = F(j, i-1) or F(j-nums[i], i-1) 

        """
        S = sum(nums)
        if S % 2 == 1:
            return False

        n, m = len(nums), S // 2
        F = [[0] * (m + 1) for _ in range(n + 1)]  # [n+1, m+1]

        for i in range(1, n+1):  # number
            for j in range(1, m+1):  # sum
                if j >= nums[i-1]:
                    F[i][j] = max(F[i-1][j], F[i-1][j-nums[i-1]] + nums[i-1])
                else:
                    F[i][j] = F[i-1][j]

        return F[n][m] == S // 2


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        """
        F(j, i) = F(j, i-1) or F(j-nums[i], i-1) 

        """
        S = sum(nums)
        if S % 2 == 1:
            return False

        n, m = len(nums), S // 2
        F = [[False] * (m + 1) for _ in range(n + 1)]  # [n+1, m+1]
        
        for i in range(n+1):
            F[i][0] = True
        for j in range(1, m+1):
            F[0][j] = False

        for i in range(1, n+1):  # number
            for j in range(1, m+1):  # sum
                if j >= nums[i-1]:
                    F[i][j] = F[i-1][j] or F[i-1][j-nums[i-1]]
                else:
                    F[i][j] = F[i-1][j]

        return F[n][m]
        