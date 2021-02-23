class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        F[j] = max(F[j-2], F[j-3]) + A[j]
        
        """
        if len(nums) == 0:
            return 0
        
        n = len(nums)
        F = [0] * n

        for i in range(n):
            if i == 0:
                F[i] = nums[0]
            elif i == 1:
                F[i] = nums[1]
            elif i == 2:
                F[i] = nums[0] + nums[2]
            else:
                F[i] = max(F[i-2], F[i-3]) + nums[i]
        
        return max(F)