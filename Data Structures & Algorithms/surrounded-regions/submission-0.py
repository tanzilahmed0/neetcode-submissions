class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        visited = set() 
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(board), len(board[0])

        def dfs(r, c): 
            if ((not 0 <= r < rows) or not (0 <= c < cols) 
                or (r, c) in visited or board[r][c] == 'X'):
                return 
            visited.add((r, c))
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc 
                dfs(nr, nc)


        for c in range(cols): 
            if board[0][c] == 'O': 
                dfs(0, c)       
            if board[rows-1][c] == 'O':
                dfs(rows-1, c)
        
        for r in range(rows): 
            if board[r][0] == 'O':
                dfs(r, 0) 
            if board[r][cols-1] == 'O':   
                dfs(r, cols-1)

        for r in range(rows): 
            for c in range(cols): 
                if (r,c) not in visited and board[r][c]== 'O': 
                    board[r][c] = 'X'
        

           


