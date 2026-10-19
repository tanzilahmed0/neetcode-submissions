import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # We can use bfs with a min heap (Djikstra's) to solve this problem 
        # We start by adding the root node to a min heap with a time of 0
        # We then visit it because it's the only node in the heap 
        # We add both of the root notes neighbor's to the heap and automatically the shortest 
        # path from root will be the root of the min heap 
        # We then visit the root of the min heap and then add it's neighbors until 
        # we visit all nodes, then we return the lognest of the shortest distances we have 
        # which is the minimum time it takes to reach all n nodes 
        # I can use a hahsmap to store distances as visited set 

        adjlist = defaultdict(list) 
        for u, v, t in times: 
            adjlist[u].append((v, t))

        heap = [] 
        distances = {} 
        heapq.heappush(heap, (0, k)) 

        while len(distances) < n and heap: 
            time, node = heapq.heappop(heap) 
            if node in distances: 
                continue
            distances[node] = time 

            for v, t in adjlist[node]: 
                heapq.heappush(heap, (t+time, v))
    
        return max(distances.values()) if len(distances) == n else -1 