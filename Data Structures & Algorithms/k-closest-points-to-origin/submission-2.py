import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        # We iterate through points and we calculate the distance from the origin 
        # and store them in a max heap of size k with the index, and then we append 
        # the indices stored in the heap to output and return it 
        heap = []

        for i in range(len(points)): 
            x, y = points[i][0], points[i][1]
            distance = math.sqrt((x - 0)**2 + (y-0)**2)

            heapq.heappush(heap,(-distance, i))
            if len(heap) > k: 
                heapq.heappop(heap)

        output = []
        for distance, idx in heap: 
            output.append(points[idx])

        return output
