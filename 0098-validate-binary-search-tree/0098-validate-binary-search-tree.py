# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        prev = None
        ans = True

        def check(node):
            nonlocal prev,ans
            if node is None:
                return True

            check(node.left)

            if prev is None:
                prev = node

            else:
                if node.val <= prev.val:
                    ans = False
                prev = node

            check(node.right)

        check(root)

        return ans