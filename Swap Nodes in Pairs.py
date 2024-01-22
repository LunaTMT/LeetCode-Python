# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)



def swapPairs(head):
    
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        first = current.next    
        second = current.next.next

        first.val, second.val = second.val, first.val

        current = current.next.next

    return dummy.next
    


arr = [1, 2, 3, 4]
head = ListNode(arr[0])
current = head
for value in arr[1:]:
    current.next = ListNode(value)
    current = current.next

swapPairs(head)