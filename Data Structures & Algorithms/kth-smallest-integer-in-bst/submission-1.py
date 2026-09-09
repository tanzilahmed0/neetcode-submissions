# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # For this solution we can do inorder traversal to recurisvely
        # add to the array in sorted order 

        array = [] 

        def inorder(node): 
            if not node: 
                return 
            
            inorder(node.left) 
            array.append(node.val)
            inorder(node.right) 
        
        inorder(root)
        return array[k-1]


        

        
            
                

        