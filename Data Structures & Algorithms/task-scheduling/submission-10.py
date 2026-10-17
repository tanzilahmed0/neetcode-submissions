from collections import Counter, deque 
import heapq 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # We want some way to store the frequencies of the characters 
        # It makes sense to start with the most frequent task and then try doing the next 
        # frequent task 
        # Each 
        # We have to have some way of tracking the curernt cooldown of each task
        # Once we process a task, ie pop from the heap, we add it to the queue, and once the cooldown period 
        # is over we can add it back to the heap 
        # "X"

        taskCount = Counter(tasks)
        heap = []
        for key, value in taskCount.items(): 
            heapq.heappush(heap, (-value, key))

        time = 0 
        queue = deque()

        while heap or queue: 
            if heap: 
                freq, task = heapq.heappop(heap)
                if freq + 1 != 0:
                    queue.append((freq+1,time+n+1,task)) 
            time += 1 
            

            if queue and time == queue[0][1]: 
                n_f, n_time, n_task = queue.popleft()
                heapq.heappush(heap, (n_f, n_task))

        return time

        # what if we just build a string and if i-n is in bounds and the top of the heap isn't in i-n of the string we can add it, for idle cycles we can just add a period and then we return length of the string
        #[(2, X), (2, Y)]