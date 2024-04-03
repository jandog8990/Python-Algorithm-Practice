# nodes contain val and next val link
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_sum(head: ListNode) -> int:
    node_sum = 0
    while head:
        node_sum += head.val
        head = head.next

    return node_sum

# create an entire linked list
one = ListNode(1)
two = ListNode(2)
th = ListNode(3)
one.next = two
two.next = th
head = one

# return the head sum
res = get_sum(head)
print(f"total sum = {res}")
