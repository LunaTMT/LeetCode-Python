# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Calculate the position to remove
        position = length - n
        
        # Reset current to the dummy node
        current = dummy
        while position > 0:
            current = current.next
            position -= 1
        
        # Remove the nth node from the end
        current.next = current.next.next
        
        return dummy.next
