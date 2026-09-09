import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        
        heapq.heapify(heap)
        while len(heap) > 1: 
            y = -1 * heapq.heappop(heap)
            x = -1 * heapq.heappop(heap)

            if x < y: 
                y -= x
                heapq.heappush(heap, -1 * y)

       
        return -1 * heap[0] if heap else 0 
            

        