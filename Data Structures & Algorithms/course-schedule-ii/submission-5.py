from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # So essentially, if there is a cycle, we cannot finish all the courses 
        # We can recursively check to see if we are able to take the course, 
        # if we can we add it to a list, if at any point there's a cycle we return an empty list 
        # our dfs function can return a boolean that will say if if we can take all the courses, and we add to a global list 
        # if it's false we return an empty list 
        adjlist = defaultdict(list)
        for course, prereq in prerequisites: 
            adjlist[course].append(prereq)

        self.output = []
        visited = set()
        completed = set()

        # {0: 1}, {1: 2}, {2: 3}    
        # We check if there's a cycle in our current dfs path
        def dfs(course, visited): 
            if course in visited: 
                return False 
            if course in completed:        
                return True 
                
            visited.add(course) 
            for prereq in adjlist[course]: 
                if not dfs(prereq, visited): 
                    return False
            visited.remove(course)
            completed.add(course)
            self.output.append(course)
            return True

        
        for course in range(numCourses): 
            if not dfs(course, visited): 
                return []
        
        return self.output

        
    

        