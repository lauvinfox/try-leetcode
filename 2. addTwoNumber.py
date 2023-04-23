def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    pointer = result
    carry = 0

    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next

        carry, val = divmod(val, 10)
        pointer.next = ListNode(val)
        pointer = pointer.next
    return result.next
