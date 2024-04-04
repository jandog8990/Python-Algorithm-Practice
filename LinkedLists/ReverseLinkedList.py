# get the middle value of linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next   # dont lose next node
        curr.next = prev        # rev direction of ptr
        prev = curr             # set prev ptr to curr 
        curr = next_node        # move to the next node

    return prev

one = ListNode(1)
one.next = ListNode(2)
one.next.next = ListNode(3)
one.next.next.next = ListNode(4)
one.next.next.next.next = ListNode(5)
res = reverse_list(one)

print("Original List:")
while one:
    print(f"one.val = {one.val}")
    one = one.next
print("\n")

print("Reversed List:")
while res:
    print(f"res.val = {res.val}")
    res = res.next
