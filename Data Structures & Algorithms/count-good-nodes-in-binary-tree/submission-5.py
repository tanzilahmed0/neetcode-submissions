# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # What's considered a good node?
        count = 0
        def dfs(node, maxVal): 
            nonlocal count 
            if not node: 
                return 0 
            if node.val >= maxVal: 
                count += 1 
            maxVal = max(maxVal, node.val)
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        
        
        dfs(root, float('-inf'))
        return count 
        