
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Union find 
        parent = list(range(n))


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

        # To check connectivity, we can just see if the length of edges is equal to how many nodes we have 
        if len(edges) != n-1: 
            return False
        
        # So we iterate through edges, and we connect all the neighbors, so if we try running union and 
        # it's already connected, then it's an invalid tree 
        # [0, 1, 2, 3, 4]
        # 0 <- 1 <- 2 <- 3
        for u, v in edges: 
            if not union(u, v): 
                return False 

    
        
        return True 

        