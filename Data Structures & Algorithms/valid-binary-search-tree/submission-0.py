# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # We can recursively check every node to see if it falls between
        # lower and upper bound 
      
        
        def valid(node, left, right): 
            if not node: 
                return True 
            
            if not(left < node.val < right):
                return False  
                
            return (valid(node.left, left, node.val) 
                    and valid(node.right, node.val, right))

        return valid(root, float('-inf'), float('inf'))
        

            
        
            

            
        