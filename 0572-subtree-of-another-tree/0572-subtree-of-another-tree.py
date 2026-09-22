# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if subRoot is None:
            return True

        if root is None:
            return False

        def check(root1,root2):
            if (root1== None and root2 == None):
                return True

            if (root1 == None or root2 == None):
                return False

            if (root1.val != root2.val):
                return False

            return check(root1.left, root2.left) and check(root1.right, root2.right)

        if check(root,subRoot):
            return True
            
        if self.isSubtree(root.left,subRoot):
            return True

        if self.isSubtree(root.right,subRoot):
            return True
        
        return False


