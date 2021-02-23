class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        F(j) = max(F(i)) + 1, 0 <= i < j and nums[i] < nums[j]
        
        """
        n = len(nums)
        F = [0] * n
        
        F[0] = 1
        for i in range(1, n):
            sub_lengths = [0]
            for j in range(0, i):
                if nums[j] < nums[i]:
                    sub_lengths.append(F[j])
            F[i] = max(sub_lengths) + 1
            
        return max(F)