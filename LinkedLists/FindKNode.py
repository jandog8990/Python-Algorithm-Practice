# nodes contain val and next val link
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# find the kth node using slow/fast pointers
def find_node(head: ListNode, k: int) -> ListNode:
    slow = head
    fast = head

    # ffwd the fast node by k
    for _ in range(k):
        fast = fast.next
        print(f"fast.val = {fast.val}")
    print("\n")

    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        print(f"slow.val = {slow.val}")
        print(f"fast.val = {fast.val}")
        print("\n")
    return slow

one = ListNode(1)
one.next = ListNode(2)
one.next.next = ListNode(3)
one.next.next.next = ListNode(4)
one.next.next.next.next = ListNode(5)

res = find_node(one, 2)
print(f"Res = {res.val}")
