from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Union find 
        parent = list(range(n))

        print(parent)
        def find(x):
            if parent[x] != x: 
                parent[x] = find(parent[x]) 
            
            return parent[x]

        # Union connects two components
        def union(x, y):    
            rootX = find(x)
            rootY = find(y) 

            # If they have the same root, they're already connected 
            if rootX == rootY: 
                return False 
            
            # You'll make one of the roots a subtree of the other 
            parent[rootY] = rootX
            return True 
        
        # So we iterate through edges, and we connect all the neighbors, so if we try running union and 
        # it's already connected, then it's an invalid tree 
        # [0, 1, 2, 3, 4]
        # 0 <- 1 <- 2 <- 3
        for u, v in edges: 
            if not union(u, v): 
                return False 

        root = find(0)
        for i in range(1, n): 
            if find(i) != root: 
                return False
        
        return True 

        