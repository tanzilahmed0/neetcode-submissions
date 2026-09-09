import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # We initalize a heap that's just nums 
        self.k = k
        self.heap = nums
        # We only want a min heap of size k, because we only care about 
        # max the k largest elements. Any elements less than the kth largest
        # is irrelevant
        heapq.heapify(self.heap)
        # So we pop while the length of the heap is greater than k
        while len(self.heap) > k: 
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        # We just add the value to the heap
        # and pop the minimum to still have the k largest
        # We don't want to pop from the heap if it has less than k elements
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
        # the k largest element is just the first element of min heap
        return self.heap[0]
        

        

        
