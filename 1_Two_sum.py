class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}  # left: index
        
        for i, n in enumerate(nums):
            if n in mapping:
                return [i, mapping[n]]
            else:
                mapping[target - n] = i