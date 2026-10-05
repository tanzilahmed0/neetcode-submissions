from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Kahn's Algorithm 
        # At each course what can i do right now? 
        # Calculate the indegree i.e. the number of edges coming into a node 
        # start with nodes with indegree of 0 because that means they have no prereqs 
        adjlist = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque()
        output = []
        for course, prereq in prerequisites: 
            adjlist[prereq].append(course) 
            indegree[course] += 1 

        for i in range(len(indegree)): 
            if indegree[i] == 0: 
                queue.append(i)

        # 0 -> 1 -> 3
        # | -> 2 -> 
        while queue:
            node = queue.popleft()
            output.append(node) 

            for course in adjlist[node]: 
                indegree[course] -= 1 
                if indegree[course] == 0: 
                    queue.append(course)
            
        if len(output) != numCourses: 
            return [] 
        else: 
            return output
                


        
      

        
    

        