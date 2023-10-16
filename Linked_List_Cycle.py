def hasCycle(self, head: Optional[ListNode]) -> bool:
    found = defaultdict(int)
    while head:
        if head in found:
            return True
        else:
            found[head] += 1
        head = head.next
    return False