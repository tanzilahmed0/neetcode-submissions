import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We can use a max heap and iterate through stones and pop the top 
        # 2 values each time and then run our conditionals and then return the heap 
        heap = []

        for i in stones: 
            heapq.heappush(heap, -i)

        while len(heap) > 1: 
            val1, val2 = -heapq.heappop(heap), -heapq.heappop(heap)
            if val1 > val2: 
                heapq.heappush(heap, -(val1 - val2))

        if heap: 
            return -heap[0]
        else: 
            return 0