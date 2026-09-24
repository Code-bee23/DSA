# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def check(node):
            nonlocal ans

            if node is None:
                return 0

            left = check(node.left)
            right = check(node.right)

            self_boss = 0 
            if node == p or node == q:
                self_boss = 1
            
            total = left + right + self_boss

            if total == 2 and ans is None:
                ans = node
            
            return total 
        
        check(root)

        return ans