# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        res = False

        def path(node,total):
            if node is None:
                return False
            
            total += node.val

            if node.left is None and node.right is None:
                return total == targetSum

            left = path(node.left,total)
            right = path(node.right,total)

            return left or right

        return path(root,0)