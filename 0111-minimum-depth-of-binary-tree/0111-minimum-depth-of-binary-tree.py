# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        #if the root is null 
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        #if both left and right child is None then return 1
        if root.left is None and root.right is None:
            return 1
        
        #if left child is null then add one to the right depth
        if root.left is None:
            return 1 + right_depth
        
        #if right child is null then add one to the left depth
        if root.right is None:
            return 1 + left_depth
        
        #at last return the min. of both left and right child and one in it 
        return 1 + min(left_depth , right_depth)