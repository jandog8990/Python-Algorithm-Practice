# nodes contain val and next val link
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# swap pairs of nodes using pointers for
# every other node in the linked list
def swap_pairs(head: ListNode) -> ListNode:
    # check edge case: LL has 0 or 1 node => return 
    if not head or not head.next:
        return head

    # we will work backwards in the steps
    dummy = head.next   # Step 5: dummy reference to return node
    prev = None         # set prev pointer
    while head and head.next:
        print(f"curr head.val = {head.val}") 
        if prev:
            # Step 4: set the prev.next to head.next (ex: A -> D) 
            head_next = head.next 
            prev.next = head_next 
            print(f"prev.next = head.next = {head_next.val}") 

        # Step 3: set previous node = curr node
        prev = head
        print(f"prev = head = {prev.val}")

        # Step 2: set the next node to the head.next.next (A->B->[C])
        next_node = head.next.next  # ex: C
        if (next_node != None):
            print(f"next_node = head.next.next = {next_node.val}")
        else:
            print(f"next_node = {next_node}") 

        # Step 1: set the head.next.next to current head (C to A)
        head.next.next = head
        print(f"head.next.next = head = {head.val}")

        # Step 6: handle case with odd # of nodes
        head.next = next_node
        head = next_node # move to next pair
        if (next_node != None):
            print(f"head = next_node = {head.val}") 
        else:
            print(f"head = next_node = {head}") 
        print("\n")

    return dummy

one = ListNode(0)
one.next = ListNode(1)
one.next.next = ListNode(2)
one.next.next.next = ListNode(3)
one.next.next.next.next = ListNode(4)
one.next.next.next.next.next = ListNode(5)
"""
head = one

print(f"Original Linked List:")
while head:
    print(f"head.val = {head.val}")
    head = head.next
print("\n")
"""

res = swap_pairs(one)
print(f"Swapped pairs Linked List:")
while res:
    print(f"res.val = {res.val}")
    res = res.next
print("\n")
