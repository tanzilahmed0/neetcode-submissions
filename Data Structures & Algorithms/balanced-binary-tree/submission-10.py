# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # So first, we can think of this recursively and look at each node, what do we want it to return? 
        # We want our dfs function to return the height of the current node
        # and then we can check if the difference of the right and left is > 1, if is return false
        # if not return true 
        self.balance = True 
        def dfs(node): 
            if not node: 
                return 0 
            
            left = dfs(node.left) 
            right = dfs(node.right) 

            if abs(left - right) > 1: 
                self.balance = False 
            return 1 + max(left, right)

        dfs(root) 
        return self.balance

        