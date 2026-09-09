from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)

        # Map courses to their prereqs
        for course, prereq in prerequisites: 
            adjlist[course].append(prereq)
        # 0 = unvisited, 1 = visiting, 2 = visited
        states = [0] * numCourses
        output =[]
        
        # Dfs returns true if no cycle, else
        def dfs(course):
            # If we encounter a neighbor that's in visiting, we detected a cycle 
            if states[course] == 1: 
                return False
            # if we already visited course, return True
            elif states[course] == 2: 
                return True
            # Set current state to visited
            states[course] = 1 
            # Check all of its neighbors
            for prereq in adjlist[course]: 
                if not dfs(prereq): 
                    return False
            # Once we check all of its neighbors, we can mark it as visited
            states[course] = 2
            output.append(course)
            return True
        

        for i in range(numCourses): 
            if not dfs(i):
                return []
        
        return output


