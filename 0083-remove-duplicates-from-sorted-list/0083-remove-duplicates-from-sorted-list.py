class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # Linked List -> Array
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        res = []
        for num in arr:
            if not res or res[-1] != num:
                res.append(num)

        # Array -> Linked List 
        dummy = ListNode(0)
        curr = dummy

        for num in res:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next