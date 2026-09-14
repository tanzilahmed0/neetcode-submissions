# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # We can have a recursive dfs function that goes through each node and returns if 
        # it's a good node. and we increment the count of good nodes by 1 each time
        # At each node, we carry up the max value we have seen so far down that path 
        # So at 3, we return up 3 max value. if previous node is bigger, it's not a good node

        self.good = 0 

        def dfs(node, maxVal): 
            if not node: 
                return 
            if node.val >= maxVal: 
                self.good += 1 

            maxVal = max(node.val, maxVal)

            dfs(node.left, maxVal) 
            dfs(node.right, maxVal)

            return maxVal
        
        dfs(root, root.val)
        return self.good
       
        