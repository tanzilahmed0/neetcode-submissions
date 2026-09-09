# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # For level order traversal we need a list to hold the result 
        result = [] 
        # We initialize a deque init to hold the root
        queue = deque([root]) 
        if not root: 
            return result

        # Keep going while there are nodes to process
        while queue: 
            # To store the nodes we pop
            level = []
            # len method evaluates length of queue at the start so when you add the childrne 
            # it doesnt behave as if it's part of the same level
            for i in range(len(queue)): 
                # Pop the nodes in the queue and add to empty list level
                node = queue.popleft()
                level.append(node.val)
                # If the node has a left and right child, we add it to the queue 
                if node.left: 
                    queue.append(node.left) 
                if node.right: 
                    queue.append(node.right) 
            result.append(level)
        
        return result

            
