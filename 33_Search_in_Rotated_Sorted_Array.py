class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findThePivot(nums)
        sorted_arr = nums[pivot:] + nums[:pivot]
        index = self.binarySearch(sorted_arr, 0, len(sorted_arr)-1, target)
        if index == -1:
            return -1
        else:
            return (index + pivot) % len(nums)
        
    def findThePivot(self, nums: List[int]):
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return l

    def binarySearch(self, arr, l, r, x):
        if r >= l:
            mid = l + (r - l) // 2

            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binarySearch(arr, l, mid-1, x)
            else:
                return self.binarySearch(arr, mid+1, r, x)
        else:
            return -1

