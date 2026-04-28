class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        area = 0
        while left < right:
            distance = right - left 
            area = max(area, (min(heights[left], heights[right]) * distance))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area
#this solution is o(n) time where n is the size of the list heights
#intuition: while moving our pointers we decide which one moves based on the min height. the width will continue to decrease. the only way for the area to increase is if we get rid of the shorter wall to try and increase the min height
