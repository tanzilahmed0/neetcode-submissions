# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Per node, is it between p and q, if it is, then it's the LCA 
        # If p and q are both greater, then the LCA must be in the right subtree
        # If p and q are both less, then the LCA must be in the left subtree

        if not root or not p or not q: 
            return None 
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else: 
            return root 
        
    
            


