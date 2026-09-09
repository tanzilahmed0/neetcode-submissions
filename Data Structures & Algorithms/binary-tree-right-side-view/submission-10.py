# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If we a do a bfs traversal on the tree, 
        # the last node added to the queue is the right most node already 
        queue = deque([root]) 
        output = []

        if not root: 
            return []
        

        while queue:
            right = queue[-1]
            output.append(right.val)
            for i in range(len(queue)): 
                node = queue.popleft()
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
    

        return output
        
            
        