# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # How can we clean up this solution 
        if not root: 
            return 0
    
        queue = deque([(root, root.val)]) 
        # Each node's comaprison only 
        count = 0 
        while queue: 
            node, maxVal = queue.popleft()
            if node.val >= maxVal: 
                count += 1 
            maxVal = max(maxVal, node.val) 

            if node.left: 
                queue.append((node.left, maxVal))
            if node.right: 
                queue.append((node.right, maxVal))

        return count

            



        
                
        