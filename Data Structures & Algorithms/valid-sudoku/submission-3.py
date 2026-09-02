class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] != ".":
                    if board[row][i] in seen:
                        return False
                seen.add(board[row][i])
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] != ".":
                    if board[i][col] in seen:
                        return False
                seen.add(board[i][col])

        for box in range(9):
            seen= set()
            #this is developed using the formula box = (start_row//3)  * 3 + start_col
            #start_col can be classified as a "remainder" to the box equation which can be used as a %
            start_row = (box // 3)*3
            start_col = (box % 3) *3
            for i in range(3):
                for j in range(3):
                    r = start_row + i
                    c = start_col + j
                    if board[r][c] != ".":
                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c])
        return True
