class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #two pointers, find midpoint, update a pointer based on the target
        l = 0
        r = len(nums)-1
        while l <= r:
            midpoint = r - l
            if target > nums[midpoint]:
                l= midpoint + 1
            elif target < nums[midpoint]:
                r = midpoint -1
            else:
                return midpoint
        return -1
        #worst case o(logn) time where n is the length of nums, constant space