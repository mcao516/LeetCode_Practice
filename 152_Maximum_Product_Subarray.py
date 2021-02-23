class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        F(j) = max(F(j - 1) * nums[j], nums[j])
        F(j) = min(F(j - 1) * nums[j], nums[j])
        
        """
        n = len(nums)
        F_max, F_min = [0] * n, [0] * n
        
        F_max[0], F_min[0] = nums[0], nums[0]
        for i in range(1, n):
            candidates = (F_min[i-1] * nums[i], F_max[i-1] * nums[i], nums[i])
        
            F_max[i] = max(candidates)
            F_min[i] = min(candidates)
        
        return max(F_max)