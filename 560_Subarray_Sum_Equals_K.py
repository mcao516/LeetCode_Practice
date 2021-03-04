class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = {}
        
        total_sum, count = 0, 0
        for i in range(len(nums)):
            if total_sum in pre_sum:
                pre_sum[total_sum] += 1
            else:
                pre_sum[total_sum] = 1
                
            total_sum += nums[i]
            
            if (total_sum - k) in pre_sum:
                count += pre_sum[(total_sum - k)]
                
        return count