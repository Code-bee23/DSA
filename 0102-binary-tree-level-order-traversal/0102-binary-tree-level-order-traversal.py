# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        curr_level = [root]
        res = []

        while curr_level:
            res.append([node.val for node in curr_level])
            next_level = []
            
            for node in curr_level :
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

                curr_level = next_level

        return res
        