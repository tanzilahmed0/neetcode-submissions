# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # from preorder we know that hte first index is the root 
        # From inorder traversal, we know that the values on the left of where the root is 
        # is left subtree and the ones that are part of the right subtree are on the right of root in inorder
        # the one on the left subtree are 
        # If we have a hashmap where we store the indices of inorder, we can build a tree 
        # from the partition of the subarray to the left of the root and the subarray to the right of the root 
        # We need to move the partition index each time      

        self.preorderIndex = 0 
        inorderMap = {}
        for i, element in enumerate(inorder): 
            inorderMap[element] = i 
        
        # So i have an index that is basically the current root, create a dict that maps inorder elements 
        # to their index so i can find where the root is in inorder which is the pivot 
        # We built the root node at that vale
        # We then move the preorder index because that next element is the root of the left subtree
        # so then we can recursively build the left subtree from the original lower bound to 
        # where the preorderindex was in the inorder array and do the same for the right subtree
        # and then we return the root 

        def buildNode(left, right): 
            if left > right: 
                return None

            rootVal = preorder[self.preorderIndex]
            newRoot = TreeNode(rootVal)

            self.preorderIndex += 1

            newRoot.left = buildNode(left, inorderMap[rootVal]-1)
            newRoot.right = buildNode(inorderMap[rootVal] + 1, right)

            return newRoot 

        return buildNode(self.preorderIndex, len(preorder) - 1)




        
        