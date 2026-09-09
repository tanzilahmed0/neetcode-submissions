# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # We obviously want to do dfs to find the max depth
        if not root: 
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        
        