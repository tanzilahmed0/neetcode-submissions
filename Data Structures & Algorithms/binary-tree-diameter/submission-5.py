# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # What is the diameter of a binary tree?? 
        # so at each node, we want to return up it's current height 
        # but the diameter is the height of the left and right subtrees 
        # So we can store the maxDiameter that updates 
        # We can recursively do dfs and at each node return the height, and then 
        # say the maxDiameter is the max of current max and left + right subtree height 

        self.maxDiameter = 0
        def dfs(node): 
            if not node: 
                return 0 
            
            left = dfs(node.left)
            right = dfs(node.right) 

            self.maxDiameter = max(self.maxDiameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.maxDiameter
        