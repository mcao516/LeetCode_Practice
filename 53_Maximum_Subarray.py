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

#     def maxSubArray(self, nums: List[int]) -> int:
#         # find the subproblem
#         # K(i) = (K(i+1) > 0 ? K(i+1) : 0) + A[i]
#         n = len(nums)
#         K = [0] * n
        
#         K[n-1] = nums[n-1]
#         for i in range(1, n):
#             if K[n-i] > 0:
#                 K[n-i-1] = K[n-i] + nums[n-i-1]
#             else:
#                 K[n-i-1] = nums[n-i-1]
        
#         return max(K)