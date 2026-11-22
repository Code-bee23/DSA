# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        # Find middle
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split linked list
        prev.next = None

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)

        # Merge sorted halves
        return self.merge(left, right)

    def merge(self, left, right):

        dummy = ListNode(0)
        current = dummy

        while left and right:

            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # Attach remaining nodes
        if left:
            current.next = left

        if right:
            current.next = right

        return dummy.next