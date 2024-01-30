def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:

        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        sum_ = x + y + carry 
        carry = sum_ // 10

        current.next = ListNode(sum_ % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next