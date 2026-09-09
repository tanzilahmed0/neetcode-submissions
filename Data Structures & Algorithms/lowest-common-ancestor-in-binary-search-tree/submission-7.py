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

        def dfs(node): 
            if not node: 
                return 
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val: 
                return node 
            if p.val > node.val and q.val > node.val:
                return dfs(node.right) 
            else: 
                return dfs(node.left) 

        return dfs(root)
            


