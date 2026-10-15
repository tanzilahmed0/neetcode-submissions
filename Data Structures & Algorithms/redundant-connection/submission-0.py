from collections import Counter 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # We can run union find through edges, and when we encounter an edge that already has been joined 
        # and has the same root, we can update the edge we return, if we encounter a later one 
        # we update it 
        n = len(edges)
        parent = list(range(n+1))

        edge = None 
        def find(x): 
            if parent[x] != x: 
                return find(parent[x]) 
            return x

        def union(x, y): 
            rootX = find(x)
            rootY = find(y) 

            if rootX == rootY: 
                return False 
            
            parent[rootY] = rootX
            return True 

        for u, v in edges: 
            if not union(u, v): 
                edge = [u,v]

        return edge

        
        