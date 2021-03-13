class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            n = abs(n)
            if nums[n-1] > 0:
                nums[n-1] = -nums[n-1]
                
        outputs = []
        for i in range(len(nums)):
            if nums[i] > 0:
                outputs.append(i+1)
        return outputs