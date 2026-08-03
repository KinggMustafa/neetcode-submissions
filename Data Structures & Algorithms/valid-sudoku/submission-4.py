class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #each row must contain digits 1-9 without duplicates

        for row in board:
            setcol = set()
            for col in row:
                if col == '.':
                    continue
                elif col in setcol:
                    return False
                else:
                    setcol.add(col)
        #each col must contain digits 1-9 so same thing but for columns

        for col in range(9):
            setcols = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                elif board[row][col] in setcols:
                    return False
                else:
                    setcols.add(board[row][col])
        #condition 3, how do we get the 3x3 boxes


        gridmap = defaultdict(set) #key will be our which 3,3 in our 9x9 grid, using a tuple,our value will be a set, if its in the set, return False
        for row in range(9):
            for col in range(9):
                grid = (row//3, col//3)
                if board[row][col] == '.':
                    continue
                elif board[row][col] in gridmap[grid]:
                    return False
                else:
                    gridmap[grid].add(board[row][col])
        return True

        #O(n^2) time and o(n) space


