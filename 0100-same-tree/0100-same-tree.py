# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def check(root1,root2):

            if (root1== None and root2 == None):
                return True

            if (root1 == None or root2 == None):
                return False

            if(root1.val != root2.val):
                return False

            r1 = check(root1.left , root2.left)

            r2 = check(root1.right , root2.right)

            if(r1 == True and r2 == True):
                return True

            return False

        return check(p , q)