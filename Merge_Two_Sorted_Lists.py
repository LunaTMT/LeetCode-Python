
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    cur = dummy = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1, cur = l1.next, l1
        else:
            cur.next = l2
            l2, cur = l2.next, l2
        
    if l1 or l2:
        cur.next = l1 if l1 else l2
    
    return dummy.next

mergeTwoLists(l1 = [1,2,4], l2 = [1,3,4])