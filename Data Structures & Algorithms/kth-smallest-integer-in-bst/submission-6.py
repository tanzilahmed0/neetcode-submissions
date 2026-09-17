# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Can't you just traverse the tree inorder traversal then add to a list and return k-1 index of that 
        self.result = [] 

        def inorder(node): 
            if not node or len(self.result) >= k: 
                return 
            
            inorder(node.left)
            self.result.append(node.val)
            inorder(node.right)

        inorder(root)
        return self.result[k-1]
        