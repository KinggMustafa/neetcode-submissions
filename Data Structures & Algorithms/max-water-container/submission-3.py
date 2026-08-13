class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        res = float('-INF')
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            res = max(res, width * height)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res
#o(n) time where n is the length of heights, constant space