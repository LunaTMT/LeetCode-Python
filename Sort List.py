
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Find the middle of the linked list
        mid = self.find_middle(head)
        right_head = mid.next
        mid.next = None  # Split the linked list into two halves
        
        # Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(right_head)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def find_middle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        if left:
            current.next = left
        elif right:
            current.next = right
        
        return dummy.next
                
                



        