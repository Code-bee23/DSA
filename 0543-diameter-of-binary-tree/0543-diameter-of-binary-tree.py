# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def check(node):
            nonlocal res

            if node is None:
                return 0

            left = check(node.left)
            right = check(node.right)

            total = left + right

            res = max(res, total)

            return 1 + max(left, right)

        check(root)

        return res
