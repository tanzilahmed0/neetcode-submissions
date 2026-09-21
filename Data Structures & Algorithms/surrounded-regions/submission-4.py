class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # What if we do one pass on every O on the borders and do dfs and makr them as visited 
        # Then we iterate on the non border cells and check if it's visited meaning it's border ajacent 
        # if it's not, then we change it to an X 
        # 

        directions = [(1, 0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c): 
            if not 0 <= r < rows or not 0 <= c < cols or board[r][c] == 'X' or (r,c) in visited: 
                return 
            
            visited.add((r,c))
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc 
                dfs(nr, nc)       

        for r in range(rows): 
            dfs(r, 0)
            dfs(r, cols-1)
        for c in range(cols): 
            dfs(0, c)
            dfs(rows-1, c)

        for r in range(1, rows-1): 
            for c in range(1, cols-1): 
                if board[r][c] == 'O' and (r,c) not in visited: 
                    board[r][c] = 'X'

        