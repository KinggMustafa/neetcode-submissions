class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while l <= r:
            midpoint = (l + r) //2
            if target < matrix[midpoint][0]:
                r = midpoint -1
            elif target > matrix[midpoint][-1]:
                l = midpoint + 1
            else:
                left = 0
                right = len(matrix[midpoint])-1
                row = matrix[midpoint]
                while left <= right:
                    mid = (left + right)//2
                    if target == row[mid]:
                        return True
                    elif target < row[mid]:
                        right = mid -1
                    else:
                        left = mid + 1
                return False
        return False

        #o(logn) because we continiously cut our search in half