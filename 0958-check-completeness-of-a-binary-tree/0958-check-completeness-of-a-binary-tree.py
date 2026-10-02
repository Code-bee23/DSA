# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
    
        if root is None:
            return True

        q = deque()
        q.append(root)
        
        none_found = False

        while q:
            t = q.popleft()

            if t is None:
                none_found = True

            else:
                if none_found == True:
                    return False

                q.append(t.left)
                q.append(t.right)

        return True