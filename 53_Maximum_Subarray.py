class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # K(i): maxSubArray for A[0:i] which must has A[i] as the end element
        # K(i) = (K(i-1) > 0 ? K(i-1) : 0) + A[i]
        n = len(nums)
        K = [0] * n
        
        K[0] = nums[0]
        for i in range(1, n):
            if K[i-1] > 0:
                K[i] = K[i-1] + nums[i]
            else:
                K[i] = nums[i]
        
        return max(K)


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        F[i] = max(F[i-1], nums[i])
        
        """
        n = len(nums)
        F = [0] * n
        
        F[0] = nums[0]
        for i in range(1, n):
            F[i] = max(F[i-1] + nums[i], nums[i])
            
        return max(F)