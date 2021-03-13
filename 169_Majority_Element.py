import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        vote = 1
        
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                vote += 1
            else:
                vote -= 1
                
            if vote == 0:
                candidate = nums[i]
                vote = 1
                
        return candidate


# class Solution2:
#     def majorityElement(self, nums: List[int]) -> int:
#         majority_count = len(nums) // 2
        
#         while True:
#             candidate = random.choice(nums)
#             if sum(1 for n in nums if n == candidate) > majority_count:
#                 return candidate