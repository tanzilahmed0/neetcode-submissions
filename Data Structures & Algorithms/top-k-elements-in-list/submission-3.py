import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top k, i'm thinking of using a heap
        # We can heapify nums and then pop the k items 
        # We need a frequency map 

        freqs = Counter(nums) 

        heap = [] 
        for key, value in freqs.items(): 
            heapq.heappush(heap, (-value, key))

        result = [] 
        for i in range(k): 
            value, key = heapq.heappop(heap) 
            result.append(key)
        
        return result