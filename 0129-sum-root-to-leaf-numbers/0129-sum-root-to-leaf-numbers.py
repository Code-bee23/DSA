# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        res = 0
        def numbers(node,total):
            nonlocal res
            if node is None:
                return 

            total = total*10 + node.val

            if node.left is None and node.right is None:
                res += total
                return

            numbers(node.left,total)
            numbers(node.right,total)

        numbers(root,0)

        return res