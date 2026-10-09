class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        # Essentially we're trying to find the number of groups 
        # One solution is doing a dfs at each node and visiting all neighbors and then u increment a count 
        # after each iteration 
        # We can also do union find and then find the roots of all nodes 
        # turn it into a set and then return the length of the set 

        parent = list(range(n))

        def find(x): 
            if parent[x] != x:  
                parent[x] = find(parent[x])
            
            return parent[x] 

        count = 0
        
        def union(x, y): 
            rootX = find(x)
            rootY = find(y) 

            if rootX == rootY: 
                return False 

            parent[rootY] = rootX
            return True 
        
        # parent: [0, 0, 0, 2]
        # 
        for u, v in edges: 
            union(u, v)

        for i in range(n): 
            find(i)

        return len(set(parent))