from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # [0,1] [1, 3], [3, 4], [5, 6]
        # 0 -> 1 - > 3 -> 4 -> 1 
        # 5 -> 6
        # Essentially if there is a cycle, we can't finish all courses, 
        # So we can go through adjacency list and recursively go through each connected edge 
        # we can use a visited set to track if we've run into the same course, which means it's not possible as the 
        # courses are prereqs of each other

        adjlist = defaultdict(list)
        visited = set()

        for a, b in prerequisites: 
            adjlist[a].append(b)
        
        def dfs(course, visited): 
            if course in visited: 
                return False
            if adjlist[course] == []:
                return True

            visited.add(course) 
            for prereq in adjlist[course]: 
                if not dfs(prereq, visited): 
                    return False
            visited.remove(course)
            adjlist[course] = []
            return True
        
        for course in range(numCourses): 
            if not dfs(course, visited): 
                return False 
        return True


            
