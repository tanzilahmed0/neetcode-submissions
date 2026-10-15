from collections import defaultdict, deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adjlist = defaultdict(list) 
    
        def dfs(node, parent): 
            # If we've already vistied a node, it's a cycle 
            if node in visited: 
                return True 
            visited.add(node)
            for neighbor in adjlist[node]:
                # If one of neighbors is its parent, it's a connected component, so we skip it 
                if neighbor == parent: 
                    continue 
                if dfs(neighbor, node): 
                    return True 

            return False

        
        for u, v in edges: 
            adjlist[u].append(v)
            adjlist[v].append(u)
            visited = set()

            if dfs(u, -1): 
                return [u, v]
        
        return []



        

        
        