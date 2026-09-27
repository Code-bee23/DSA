# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
       
        count = 0
        answer = 0

        def check(node):

            nonlocal count , answer
            if node is None:
                return 

            check(node.left)

            count += 1

            if count == k:
                answer = node.val

            check(node.right)

        check(root)

        return answer

            