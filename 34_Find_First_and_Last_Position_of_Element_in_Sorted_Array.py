class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        index = self.binarySearch(nums, 0, n-1, target)
        if index == -1:
            return [-1, -1]
        else:
            left_pos = self.binarySearchBoundary(nums, 0, n-1, target, True)
            right_pos = self.binarySearchBoundary(nums, 0, n-1, target, False)
            
            if nums[left_pos] != target:
                left_pos += 1
                
            if nums[right_pos] != target:
                right_pos -= 1
                
            return [left_pos, right_pos]

        
    def binarySearchBoundary(self, nums: List[int], l: int, r: int, target: int, to_left: bool):
        while r - l > 1:
            mid = l + (r - l) // 2
            
            if nums[mid] < target:  # nums[l] will never be larger than target
                l = mid
            elif nums[mid] > target:  # nums[r] will be equal to target
                r = mid
            else:
                if to_left:
                    r = mid
                else:
                    l = mid
                
            # The loop wil shrink until r - l == 1
        
        if to_left:
            return l
        else:
            return r

        
    def binarySearch(self, nums: List[int], l: int, r: int, target: int):
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return -1
