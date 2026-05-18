class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix)-1
        while t <= b:
            midrow = (b + t)//2
            if target > matrix[midrow][-1]:
                t = midrow + 1
            elif target < matrix[midrow][0]:
                b = midrow - 1
            else:
                l = 0
                r = len(matrix[midrow])-1
                while l <= r:
                    midpoint = (r + l)//2
                    if target < matrix[midrow][midpoint]:
                        r = midpoint - 1
                    elif target > matrix[midrow][midpoint]:
                        l = midpoint + 1
                    else:
                        return True
                return False
        return False

        #o(log(n *m )) where n and m are the number of rows and columns
        #constant space