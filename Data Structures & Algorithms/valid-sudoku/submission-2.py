class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            setrows = set()
            for col in row:
                if col != '.':
                    if col in setrows:
                        return False
                    else:
                        setrows.add(col)
        #check cols
        for col in range(9):
            setcols = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in setcols:
                        return False
                    else:
                        setcols.add(board[row][col])
        #check the 3x3 grids using floor division, and dictionarys
        groupedgrids = defaultdict(set)
        for row in range(9):
            for col in range(9):
                key = (row // 3, col // 3) #the key to our dict, is the ordered pair grid number so row4, col4 is (1,1) the middle
                if board[row][col] != '.':
                    if board[row][col] in groupedgrids[key]:
                        return False
                    else:
                        groupedgrids[key].add(board[row][col])
        return True
        #constant time and space if it stays 9x9 but time is o(n^2), and space is (n^2) because grouped grids worst case can have 9 grids, with up to 9 characters per set so 81 so n^2
                