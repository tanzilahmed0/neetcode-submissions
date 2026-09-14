from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # Another way to think of the right side of a binary tree is that it's the last 
        # node at each level 
        # So what we can do is do a bfs and append the last node in the queue at each level 
        # and return that 
        result = [] 
        if not root: 
            return result 
        queue = deque([root]) 

        while queue: 
            level = len(queue) 
            result.append(queue[-1].val)

            for i in range(level): 
                node = queue.popleft()

                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)

        
        return result



        