# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # What do we have to check?, is the root node of the current subtree
        # the same as subroot 

        # Base Cases
        # If the subroot is empty, it is trivially a subroot of root
        if not subRoot: 
            return True
        # if root is empty, subroot can't possible be a subtree of it
        if not root and subRoot: 
            return False   

        # Helper function to check if the trees are equal
        def isSameTree(p, q): 
            if not p and not q: 
                return True

            if not p or not q or p.val != q.val: 
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        # Check if the current subtree is equal
        # Recursively call isSubtree to left and right subtrees
        return (isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) 
        or self.isSubtree(root.right, subRoot))

        
       
        