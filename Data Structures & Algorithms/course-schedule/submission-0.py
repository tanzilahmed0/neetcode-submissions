from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list) 
        # map adjacency list 
        for course, prereq in prerequisites: 
            adjlist[course].append(prereq)
        
        # Visiting states for nodes
        # 0 = unvisited, 1 = visiting, 2 = visited
        states = [0] * numCourses

        def dfs(course): 
            # If the course we're at is currently being visited,
            # a cycle has been detected, return False 
            if states[course] == 1: 
                return False 
            # If it has been fully visited, no cycles, return True
            if states[course] == 2: 
                return True 
            # Mark state as visiting
            states[course] = 1
            # Check all of its prereqs to see if its neighbors have a path that leads 
            # to itself (a back edge) 
            for i in adjlist[course]: 
                if not dfs(i):
                    return False
            # If none of the neighboring nodes are currently being visited, 
            # we mark current node as visited and return True to ensure this path is safe
            states[course] = 2
            return True
        
        for i in range(numCourses): 
            if not dfs(i):
                return False
        return True