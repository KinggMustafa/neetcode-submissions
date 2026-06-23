class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1
        while l <= r:
            midpoint = (l+r)//2
            if nums[midpoint]==target:
                return midpoint
            if nums[l] <= nums[midpoint]:
                if target >= nums[l] and target < nums[midpoint]:
                    r = midpoint -1
                else:
                    l = midpoint + 1
            elif nums[r] >= nums[midpoint]:
                if target <= nums[r] and target > nums[midpoint]:
                    l = midpoint + 1
                else:
                    r = midpoint -1
        return -1
