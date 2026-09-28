# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        g1first = None
        g1second = None

        galat = 0

        g2first = None
        g2second = None

        def check(node):
            nonlocal prev,galat,g1first,g1second,g2first,g2second
            if node is None:
                return

            check(node.left)

            if prev is None:
                prev = node

            else:
                if node.val < prev.val:
                    if galat == 0:

                        g1first = prev
                        g1second = node

                        galat += 1
                    
                    else:
                        g2first = prev
                        g2second = node
                        galat += 1
                    
                prev = node

            check(node.right)

        check(root)

        if galat == 1:
            g1first.val,g1second.val = g1second.val, g1first.val
        
        else:
            g1first.val,g2second.val = g2second.val,g1first.val

        return 