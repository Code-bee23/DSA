# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def check(node):

            if node is None:
                return False

            needed = k - node.val

            if needed in seen:
                return True

            seen.add(node.val)

            return check(node.left) or check(node.right)

        return check(root) 
        