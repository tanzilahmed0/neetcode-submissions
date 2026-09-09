# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # Recursive Solution 
        # what are the base cases/when do we stop? 

        if not root: 
            return None 
            
        if p.val <= root.val <= q.val: 
            return root

        # If p and q are both less than the root, we recurse down the left subtree
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q) 
        
        # if p and q are both greater than the root, we recurse down the right subtree
        if p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q) 
        
        else: 
            return root
        
        

        