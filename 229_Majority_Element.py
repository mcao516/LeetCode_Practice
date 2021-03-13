class Solution:    
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        candidate_1, candidate_2 = nums[0], nums[0]
        vote_1, vote_2 = 0, 0
        
        for i in range(len(nums)):

            if nums[i] == candidate_1:
                vote_1 += 1
                continue
            elif nums[i] == candidate_2:
                vote_2 += 1
                continue
            
            if vote_1 == 0:
                candidate_1 = nums[i]
                vote_1 = 1
                continue
                
            if vote_2 == 0:
                candidate_2 = nums[i]
                vote_2 = 1
                continue
                
            vote_1 -= 1
            vote_2 -= 1
        
        count_1, count_2 = 0, 0
        for n in nums:
            if n == candidate_1:
                count_1 += 1
            elif n == candidate_2:
                count_2 += 1
        
        candidates = []
        if count_1 > len(nums) // 3: candidates.append(candidate_1)
        if count_2 > len(nums) // 3: candidates.append(candidate_2)
        
        return candidates