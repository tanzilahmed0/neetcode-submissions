# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # What is our base case? 
        # At each node, the value must be the same, and the depth of each subtree 
        # has to be the same 
        if not p and not q: 
            return True

        if not p or not q or p.val != q.val: 
            return False 

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)