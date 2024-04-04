# list node for current val and next
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# check for cycles using sets 
def hasCycle(head: ListNode) -> bool:
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False
