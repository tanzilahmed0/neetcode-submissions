# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        # Binary Search Tree means that values to the right are greater and values to the left 
        # are smaller 
        # The lowest common ancestor means the highest node that is in between p and q 
        # So we can recursively check from the root node, if it's between p and q, 
        # if it is that's the LCA 
        # if both values are less than that node, we need recursively check the left subtree 
        # and if vice versa we check the right subtree 

        if not root: 
            return 
        
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val: 
            return root 
        elif p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)



