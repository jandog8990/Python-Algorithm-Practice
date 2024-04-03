# nodes contain val and next val link
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# iterate using next in linked list
def get_sum(head: ListNode) -> int:
    node_sum = 0
    while head:
        node_sum += head.val
        head = head.next

    return node_sum

# recursion using linked lists
def get_sum_recursive(head: ListNode) -> int:
    if not head:
        return 0

    return head.val + get_sum_recursive(head.next)

# create an entire linked list
one = ListNode(1)
two = ListNode(2)
th = ListNode(3)
one.next = two
two.next = th
head = one

# return the head sum
res1 = get_sum(head)
print(f"total sum = {res1}")

# return the head sum using recursion
res2 = get_sum_recursive(head)
print(f"total sum rec = {res2}")
