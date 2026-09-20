# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        left_to_right = 1

        while queue:

            level = []

            # Number of nodes in current level
            size = len(queue)

            for _ in range(size):

                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level.reverse()

            result.append(level)

            left_to_right = not left_to_right

        return result