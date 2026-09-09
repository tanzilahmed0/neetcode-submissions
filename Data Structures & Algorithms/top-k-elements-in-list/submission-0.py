import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # we can use hashmap to store frequencies of all ints in nums 
        
        freqlist = {} 

        for i in nums: 
            freqlist[i] = freqlist.get(i, 0) + 1 

        heap = [(-freq, values) for values, freq in freqlist.items()]
        heapq.heapify(heap) 

        top = [] 

        for i in range(k): 
            freq, val = heapq.heappop(heap)
            top.append(val) 
        
        return top 

        

        
        