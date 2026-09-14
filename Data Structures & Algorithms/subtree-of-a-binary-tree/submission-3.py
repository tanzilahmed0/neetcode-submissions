# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # At each each node, we check if it's the same tree as the subroot 
        # if we go through the whole tree and there's no subtrees, we return false 
        # Even if the values are the same, it's not the same subtree if the root tree has an extra 
        # leaf node
        if not root and not subRoot:
            return True 
        if not root: 
            return False 

        def dfs(node1, node2): 
            if not node1 and not node2: 
                return True

            if not node1 or not node2 or node1.val != node2.val: 
                return False
            
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        
        if dfs(root, subRoot): 
            return True
        else: 
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        