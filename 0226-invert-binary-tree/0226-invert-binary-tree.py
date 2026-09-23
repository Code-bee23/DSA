# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        #swap
        root.left , root.right = root.right , root.left

        #invert left subtree
        self.invertTree(root.left)

        #invert right subtree
        self.invertTree(root.right)

        return root