# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # What makes a tree balanced? 
        # We can get the height of the left and right subtrees of each node 
        # if right - left > 1: it's not balanced 
        # We can use a recursive function to get the height 
        # then we can compare the heights of the left and right subtrees

        self.isBalanced = True 
        def dfs(curr): 
            if not curr: 
                return 0
            left = dfs(curr.left) 
            right = dfs(curr.right) 
            if right - left > 1 or left - right > 1: 
                self.isBalanced = False
            return 1 + max(left, right)
                

        dfs(root)  

        return self.isBalanced
            


            
        