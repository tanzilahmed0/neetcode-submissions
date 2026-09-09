# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iteratively with a stack 
        stack = [] 
        n = 0
        curr = root 

        # Keep going until all nodes processed
        while stack or curr: 
            # Keep going all the way left
            while curr: 
                # Before going left, add the current node to stack
                stack.append(curr)
                curr = curr.left
            # We pop once reaching all the way left, which pops us back up
            curr = stack.pop()

            n += 1 
            if n == k:
                return curr.val 

            curr = curr.right



        

        
            
                

        