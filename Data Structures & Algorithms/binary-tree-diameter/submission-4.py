# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # At each node it wants its length, so we want a helper function that gets the length of it's leaf node
        # Ok so at each node we're returning the height up to the previous node 
        # and each node we're storing the current diameter of the subtree which is the height of left and right
        # subtrees

        self.diameter = 0
        # Returns the height of the current node 
        # But calculates the max diameter of its current subtree which is the left subtree + the right subtree
        def dfs(node):
   
            if not node: 
                return 0 
                      
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.diameter


            
            

            
            

        