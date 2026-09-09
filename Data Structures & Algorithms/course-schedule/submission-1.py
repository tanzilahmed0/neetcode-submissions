from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjlist = defaultdict(list)
        for course, prereq in prerequisites: 
            adjlist[course].append(prereq) 
        print(adjlist.values())

        visiting = set()
        def dfs(course): 
            if course in visiting: 
                return False 
            if adjlist[course] == []: 
                return True 

            visiting.add(course)
            for prereqs in adjlist[course]: 
                if not dfs(prereqs): 
                    return False
            visiting.remove(course)
            adjlist[course] = []
            return True 

        for i in range(numCourses): 
            if not dfs(i): 
                return False
        return True 