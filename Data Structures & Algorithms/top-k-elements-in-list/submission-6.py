import heapq 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # the word frequency signals to me the use of some type of hashmap
        # and then we can iterate through the hashmap and add the frequency and the 
        # integer to a heap 
        # then we can return the 2 most frequent items from the heap 
        freqs = Counter(nums)
        heap = []

        for num, freq in freqs.items(): 
            heapq.heappush(heap, (freq, num))
            if len(heap) > k: 
                heapq.heappop(heap)
        
        result = [] 
        for i in range(k): 
            result.append(heap[i][1])
        return result
     
      


