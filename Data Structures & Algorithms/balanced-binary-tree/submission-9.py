# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # at each node, we can get the height of its left and right subtrees
        # and then we can we can check if they differ by more than one 
        self.isBalanced = True
        
        def dfs(node): 
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if (abs(right-left) > 1):
                self.isBalanced=False
            return 1 + max(left, right)
        
        dfs(root)
        return self.isBalanced
        

        