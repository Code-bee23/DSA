# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        previous = None
        current = slow
        
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        left = head
        right = previous
        
        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True