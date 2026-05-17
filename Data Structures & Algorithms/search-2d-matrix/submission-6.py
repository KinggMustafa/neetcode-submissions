class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0 
        b = len(matrix)-1
        while t <= b:
            midrow = (b+t)//2
            if target < matrix[midrow][0]:
                b = midrow - 1
            elif target > matrix[midrow][-1]:
                t = midrow + 1
            else:
                left = 0
                right = len(matrix[midrow])-1
                while left <= right:
                    midpoint = (right + left)//2
                    if target < matrix[midrow][midpoint]:
                        right = midpoint-1
                    elif target > matrix[midrow][midpoint]:
                        left = midpoint + 1
                    else:
                        return True
                return False
        return False
                

                    

#space, constant, worst time complexity is O(log(n*m)) where n is the number of rows, and m is the number of columns
