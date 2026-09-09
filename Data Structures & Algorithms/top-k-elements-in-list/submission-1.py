import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = {} 

        for i in nums: 
            frequencies[i] = frequencies.get(i, 0) + 1

        heap = [(-value, key) for key, value in frequencies.items()] 

        heapq.heapify(heap)

        result = []
        for i in range(k): 
            val, key = heapq.heappop(heap) 
            result.append(key)

        return result
        
        