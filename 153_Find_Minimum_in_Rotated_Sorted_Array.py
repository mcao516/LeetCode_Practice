class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
             mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        # At this point, left and right converge to a single index (for minimum value) since
        # our if/else forces the bounds of left/right to shrink each iteration:

        # When left bound increases, it does not disqualify a value
        # that could be smaller than something else (we know nums[mid] > nums[right],
        # so nums[right] wins and we ignore mid and everything to the left of mid).

        # When right bound decreases, it also does not disqualify a
        # value that could be smaller than something else (we know nums[mid] <= nums[right],
        # so nums[mid] wins and we keep it for now).

        # So we shrink the left/right bounds to one value,
        # without ever disqualifying a possible minimum

        return nums[l]