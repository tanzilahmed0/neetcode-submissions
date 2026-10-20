# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder Traversal: root -> left -> right 
        # Inorder Traversal: left -> root -> right 
        # preorder = [3, 9, 20, 15, 7]
        # inorder  = [9, 3, 15, 20, 7]
        #      3
        #.   9   20
        #.     15  7
        # In Preorder Traversal, the root is always the first index 
        # in inorder traversal, all the elements to the left of where the root is are left children
        # and all the nodes on the right are right children 
        # So that means the next node of the preorder array is the root of the left children
        # The number of nodes in left subtree is root index - 0 of inorder 
        # So that means the left subtree in preorder is preorder[root+1:inorderroot+1]
        # We can recursively identify the root in preorder, and then find the index in inorder 
        # and then split the left and right subtrees 
        # and then locate the root from preorder because it's the first index of the subtree 

        self.preorderIndex = 0
        inorderMap = {} 
        for i in range(len(preorder)): 
            inorderMap[inorder[i]] = i

        def dfs(left, right):
            if left > right: 
                return None 

            rootVal = preorder[self.preorderIndex] 
            newRoot = TreeNode(rootVal)

            self.preorderIndex += 1 
            newRoot.left = dfs(left, inorderMap[rootVal] - 1) 
            newRoot.right = dfs(inorderMap[rootVal] + 1, right)

            return newRoot 

        return dfs(self.preorderIndex, len(preorder)-1)



            
