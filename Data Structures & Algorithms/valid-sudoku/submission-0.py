class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #cond 1: 1-9 in the rows:
        for row in board:
            setnums = set()
            for number in row:
                if number != '.':
                    if number in setnums:
                        return False
                    else:
                        setnums.add(number)
        #cond 2: check the columns:
        #column must stay constant while you go through all rows
        for column in range(9):
            setnums = set()
            for row in board: #for each column we gotta go through all the rows, #easier to write it this way bc the the len of our rows and cols are the same
                if row[column] != '.':
                    if row[column] in setnums: 
                        return False
                    else:
                        setnums.add(row[column])
        #for each 3x3:
        mapp = defaultdict(set)
        #key will be which 3x3, val will be a set

        for row in range(len(board)): 
            for column in range(len(board[row])): 
                if board[row][column] != '.':
                    index = (int(row // 3), int(column // 3)) #ordered pair for key in our dictionary
                    if board[row][column] in mapp[index]:
                        return False
                    else:
                        mapp[index].add(board[row][column])
        return True
        #constant space and time if its always 9x9
        #if it was nxn:
        #time is O(n^2) where n is the number of rows x columns
        #space is O(n^2) bc we worst case we are storing all the entries of the nxn grid when doing our nxn's



