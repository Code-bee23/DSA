# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        f = {}

        for i in range(len(inorder)):
            f[inorder[i]] = i

        idx = len(postorder) - 1

        def post(low, high):
            nonlocal idx

            if low > high:
                return None

            node = TreeNode(postorder[idx])
            idx -= 1

            inorder_index = f[node.val]

            # phele right aaye ga then left bcoz we are going backward
            #postorder - left -> right -> root
            #so in backward root -> right -> left
            node.right = post(inorder_index + 1, high)
            node.left = post(low, inorder_index - 1)

            return node

        return post(0, len(inorder) - 1)