from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # This can easily be done with a bfs which naturally processes nodes level by level 
        if not root: 
            return []
        queue = deque([root])
        result = []

        while queue: 
            levelSize = len(queue) 
            level = []
            for i in range(levelSize): 
                node = queue.popleft()
                level.append(node.val)

                if node.left: 
                    queue.append(node.left) 

                if node.right: 
                    queue.append(node.right)

            result.append(level)

        return result
            
