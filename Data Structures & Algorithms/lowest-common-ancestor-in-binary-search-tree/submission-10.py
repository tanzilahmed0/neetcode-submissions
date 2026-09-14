# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # A node can be a descendant of itself 
        # This is a binary search tree, meaning all the nodes on the left are smaller 
        # and all the nodes on the right are bigger 
        # So what we can check if the current node is in between p and q, if it is, 
        # then that's the LCA 
        # if the node is greater than them both, the LCA is on the left side 
        # if it's less than them both, it's on the right side 
        # At each node, what am i returning? what am i carrying up? 
        # I don't need to use a helper function 
        # It can be itself, so we need to include the root

        if p.val <= root.val <= q.val or q.val <= root.val <= p.val or not root: 
            return root 
        elif p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        else: 
            return self.lowestCommonAncestor(root.left, p, q)
