from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Edges make up a valid tree if they're acyclic and every node is reachable from every other node 
        # We can use 
        
        adjlist = defaultdict(list) 
        for u, v in edges: 
            adjlist[u].append(v)
            adjlist[v].append(u) 

        visited = set()
        def dfs(node, parent):
            visited.add(node) 

            for neighbor in adjlist[node]: 

                # Checking the edge we came from so we skip it 
                if neighbor == parent: 
                    continue 
                
                # If a neighbor is already visited and it's not a parent, we have a cycle
                if neighbor in visited: 
                    return False 
                
                if not dfs(neighbor, node):
                    return False 
            
            return True 

        return dfs(0, -1) and len(visited) == n
            
            