# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        result = 0

        def dfs(node):

            nonlocal result

            if node is None:
                return 0, 0

            # Get information from left subtree
            left_sum, left_count = dfs(node.left)

            # Get information from right subtree
            right_sum, right_count = dfs(node.right)

            # Calculate current subtree
            total_sum = left_sum + right_sum + node.val

            total_count = left_count + right_count + 1

            # Calculate average
            average = total_sum // total_count

            # Check if current node equals average
            if node.val == average:
                result += 1

            # Give information to parent
            return total_sum, total_count

        dfs(root)

        return result