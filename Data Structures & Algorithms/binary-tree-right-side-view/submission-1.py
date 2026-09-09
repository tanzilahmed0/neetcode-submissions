# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
        output = [] 
        if not root: 
            return output
        queue = deque([root])
        while queue: 
            nodes = []
            for i in range(len(queue)): 
                node = queue.popleft()
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
                
            output.append(nodes[-1])

        return output
            
                

