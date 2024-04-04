# get the middle value of linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_middle(head: ListNode) -> int:
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next

    for _ in range(length // 2):
        head = head.next
        print(f"Head val = {head.val}")

    return head.val

# the fast pointer ffwds to the end while the
# slow is 2 behind the fast
def get_middle_fast(head: ListNode) -> int:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        print(f"slow val = {slow.val}")
        print(f"fast val = {fast.val}")
        print("\n")

    return slow.val

one = ListNode(1)
one.next = ListNode(2)
one.next.next = ListNode(3)
one.next.next.next = ListNode(4)
one.next.next.next.next = ListNode(5)

res = get_middle(one)
print(f"Res = {res}")
print("\n")

res = get_middle_fast(one)
print(f"Res fast = {res}")

