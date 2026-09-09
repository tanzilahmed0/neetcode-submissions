# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # We need to use a variable to store the max diameter 
        # and We need a helper dfs function to get the height 
        # We can add up the height of the left subtree and the right 
        # subtree to get the diameter of each node, then recursively do it 
        # for each node 
    

        self.res = 0 
        def dfs(curr):
            if not curr: 
                return 0 
            left = dfs(curr.left) 
            right = dfs(curr.right) 
            self.res = max(self.res, left + right)
            return 1 + max(left, right) 

    
        dfs(root)

        return self.res

        