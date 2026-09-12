from collections import defaultdict
class TimeMap:

    def __init__(self):
        # We can maybe use a defaultdict(list) to s
        # Essentially it is asking what the value is at the largest timestamp that is <= requested timestamp
        # We have to find the point where where timestamp becomes larger than requested
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        answer = ""

        left, right = 0, len(self.timeMap[key]) - 1 
        while left <= right: 
            middle = (left + right) // 2 
            if self.timeMap[key][middle][1] <= timestamp: 
                answer = self.timeMap[key][middle][0]
                left = middle + 1 
            else: 
                right = middle - 1 
        
        return answer
        

        
