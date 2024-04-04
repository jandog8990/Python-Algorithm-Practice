# list node for current val and next
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# find cycle in linked list using fast 
# and slow pointers (slow meet with fast)
def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(0)

res = has_cycle(head)
print(f"Resp = {res}")
