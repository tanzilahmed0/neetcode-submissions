class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary: 
            self.dictionary[key] = [] 
        self.dictionary[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        print(self.dictionary)
        if not key in self.dictionary:
            return ""
        left, right = 0, len(self.dictionary[key]) - 1
        
        result = ""

        while left <= right: 
            mid = left + (right - left) // 2 
            
            val, time = self.dictionary[key][mid]

            if time <= timestamp: 
                result = val
                left = mid + 1
                
            
            elif time > timestamp: 
                right = mid - 1 
        
        return result 
        
            

            


            
        
