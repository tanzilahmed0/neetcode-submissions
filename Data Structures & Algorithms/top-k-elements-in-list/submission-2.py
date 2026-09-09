from collections import Counter 
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) 

        heap = []
        for keys, values in counts.items(): 
            heapq.heappush_max(heap, (values, keys))

        result = []
        for i in range(k): 
            result.append(heapq.heappop_max(heap)[1])
        
        return result

        

