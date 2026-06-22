class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        while left <= right:
            midpoint = (left + right) // 2
            l = 0
            r = len(matrix[midpoint])-1
            if target < matrix[midpoint][l]:
                right = midpoint - 1
            elif target > matrix[midpoint][r]:
                left = midpoint + 1
            else:
                while l <= r:
                    mid = (l + r) // 2
                    if target < matrix[midpoint][mid]:
                        r = mid -1
                    elif target > matrix[midpoint][mid]:
                        l = mid + 1
                    else:
                        return True
                return False
        return False