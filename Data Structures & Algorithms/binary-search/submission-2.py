class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            midpoint = (l+r)//2
            if target == nums[midpoint]:
                return midpoint
            elif target < nums[midpoint]:
                r = midpoint - 1
            else:
                l = midpoint + 1
        return -1
        #O(logn) where n is the length of nums, as we cut our array, contant space