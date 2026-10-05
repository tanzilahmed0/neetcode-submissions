class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # What we can do is go through the board, and when we encounter a char that's 
        # the first char of word, we run a recursive dfs to all of it's neighbors and see if it's the next 
        # char in word, where we pass in i, if i == len(word) we know we've found the word 
        # so we cna return true 

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):         
            if not (0 <= r < rows) or not (0 <= c < cols) or (r,c) in path or board[r][c] != word[i]: 
                return False

            if board[r][c] == word[i]: 
                path.add((r, c))   

            if i == len(word) - 1: 
                return True 

            for dr, dc in directions: 
                nr, nc = r + dr, c + dc 
                if dfs(nr, nc, i+1): 
                    return True
            
            path.remove((r, c))
        
        for r in range(rows):
            for c in range(cols): 
                if dfs(r, c, 0): 
                    return True 

        return False

            

