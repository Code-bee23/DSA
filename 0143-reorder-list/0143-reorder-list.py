# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        # Step 1: Find the middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split the list
        second = slow.next
        slow.next = None

        # Step 3: Reverse the second half
        prev = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # Step 4: Merge both halves
        first = head
        second = prev

        while second:
            nextFirst = first.next
            nextSecond = second.next

            first.next = second
            second.next = nextFirst

            first = nextFirst
            second = nextSecond
