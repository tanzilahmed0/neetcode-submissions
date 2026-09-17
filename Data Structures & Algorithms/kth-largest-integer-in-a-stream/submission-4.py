import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        self.nums = nums
        for i in self.nums: 
            heapq.heappush(self.heap, i)   
            
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)  
        while len(self.heap) > self.k: 
            heapq.heappop(self.heap)  

          
        # 1, 2, 3, 3, 3, 5, 6, 7, 8
        return self.heap[0]

