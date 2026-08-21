# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                a = l1.val
            else:
                a = 0  # if any linkedlist is None before the other then it will give 0 rather than "return 0"

            if l2:
                b = l2.val
            else:
                b = 0

            total = a + b + carry

            carry = total//10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
