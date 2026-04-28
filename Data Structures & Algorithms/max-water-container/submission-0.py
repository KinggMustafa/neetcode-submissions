class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #length times our min height of our ends
        maxarea = 0
        for i in range(len(heights)):
            for j in range(len(heights)-1, i, -1):
                distance = j- i #use our index's to find the width
                area = min(heights[i], heights[j]) * distance #take the minimum height and multiply by the distance
                maxarea = max(area, maxarea)
        return maxarea
        #this solution is o(n^2) where n is the length of the list height
        #no space

            
