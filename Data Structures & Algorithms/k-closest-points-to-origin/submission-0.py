import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # We can calculate the distance of each point and map the distance to 
        # coordinate with hashmap 
        # then we pop from the heap the k closest and append the coordinates to the list

        heap = [] 
        for x, y in points: 
            distance = x ** 2 + y **2
            heapq.heappush(heap, (distance, [x,y]))
        output = []
        for i in range(k): 
            result = heapq.heappop(heap)
            output.append(result[1])
        
        return output
        

        
        