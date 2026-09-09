from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjlist = defaultdict(list) 
        for course, prereqs in prerequisites: 
            adjlist[course].append(prereqs)
        
        # We can maybe use the DFS cycle detection algorith with 3 colors or states
        # So we'll have 3 states; 0 = unvisited, 1 = visiting, 2 = visited 
        # If we run into a course that's already in visiting, 
        # we know we have a cycle and can return False 

        states = [0] * numCourses
        def dfs(course): 
            if states[course] == 1: 
                return False 
            states[course] = 1 
            for prereqs in adjlist[course]: 
                if not dfs(prereqs):
                    return False 
            states[course] = 2 
            return True 
        
        for i in range(numCourses): 
            if not dfs(i):
                return False
        return True 
