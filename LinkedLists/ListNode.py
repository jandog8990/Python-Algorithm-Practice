# nodes contain val and next val link
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# create an entire linked list
one = ListNode(1)
two = ListNode(2)
th = ListNode(3)
one.next = two
two.next = th
head = one

print(head.val)
print(head.next.val)
print(head.next.next.val)

# create a pointer using ListNode
# pointers can only be modified 
# using direct equals (ex ptr = that)
ptr = head
head = head.next
print(ptr.val)
print(head.val)
head = None
print(ptr.val)
