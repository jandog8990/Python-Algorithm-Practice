# nodes contain val and next val link
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# prev_node is node at pos i-1
def add_node(prev_node: ListNode, node_to_add: ListNode):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

# delete node at position i by shifting the next
def delete_node(prev_node: ListNode):
    prev_node.next = prev_node.next.next
