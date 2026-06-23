class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        runmin = float("INF")
        while l <= r:
            midpoint = (l+r)//2
            runmin = min(nums[midpoint], runmin)
            if nums[midpoint] > nums[r]:
                l = midpoint + 1
            else:
                r = midpoint -1
        return runmin