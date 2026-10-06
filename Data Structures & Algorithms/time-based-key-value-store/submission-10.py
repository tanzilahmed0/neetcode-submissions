from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        # They're naturally sorted, so we can do a binary search the largest timestamp <= requested timestamp 
        left, right = 0, len(self.timeMap[key]) - 1 

        while left <= right: 
            middle = (left + right) // 2 

            if self.timeMap[key][middle][1] == timestamp: 
                return self.timeMap[key][middle][0]
            elif self.timeMap[key][middle][1] > timestamp: 
                right = middle - 1 
            elif self.timeMap[key][middle][1] < timestamp:
                left = middle + 1 

        if right < 0: 
            return ""
        else: 
            return self.timeMap[key][right][0]
            
