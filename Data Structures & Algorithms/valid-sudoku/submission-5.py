from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Without duplicates signals to me using a set 
        # We can iterate through rows and columns and have a defaultdict(set) for each row
        # but we also need a set for each 3x3 grid

        rows = len(board)
        cols = len(board[0])

        rowsSet = defaultdict(set)
        colsSet = defaultdict(set)
        boxSet = defaultdict(set)

        for r in range(rows): 
            for c in range(cols): 
                if board[r][c] == '.':
                    continue
                if board[r][c] in rowsSet[r] or board[r][c] in colsSet[c] or board[r][c] in boxSet[(r//3, c//3)]: 
                    return False 
                rowsSet[r].add(board[r][c])
                colsSet[c].add(board[r][c])
                boxSet[(r//3, c//3)].add(board[r][c])

        return True