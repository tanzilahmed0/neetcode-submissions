# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # How can we clean up this solution 

    
        def dfs(curr, max_so_far): 
            if not curr: 
                return 0
            if curr.val >= max_so_far: 
                result = 1
            else: 
                result = 0
            
            max_so_far = max(max_so_far, curr.val) 

            # At each node, if it's a good node, it sets the result to 1, 
            # then you add it to the recursive result
            result += dfs(curr.left, max_so_far)
            result += dfs(curr.right, max_so_far)
            return result
        
        return dfs(root, root.val)

        
                
        