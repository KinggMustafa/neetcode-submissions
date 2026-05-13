class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = (len(heights)-1)
        maxarea = float('-INF')
        while left < right:
            #area = l * w
            l = min(heights[left], heights[right])
            w = right - left
            maxarea= max(maxarea, l*w)
            if heights[left] < heights[right]:
                left+= 1
            else:
                right -= 1
        return maxarea
        #o(n) time where n is the length of the list heights, constant space



