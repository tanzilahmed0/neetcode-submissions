from collections import defaultdict 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9): 
            for c in range(9): 
                val = board[r][c]
                if val == ".": 
                    continue 

                # grids = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[c] or val in grid[(r // 3, c // 3)]: 
                    return False 
                else: 
                    rows[r].add(val)
                    cols[c].add(val)
                    grid[(r // 3, c // 3)].add(val)
        
        return True