# doubly linked list contains pointers to prev
# as well as the next nodes
class DoubleListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# add new node at position i
def add_node(curr_node: DoubleListNode, node_to_add: DoubleListNode):
    prev_node = curr_node.prev
    node_to_add.next = curr_node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    curr_node.prev = node_to_add

# delete node at position i
def delete_node(curr_node: DoubleListNode):
    prev_node = curr_node.prev
    next_node = curr_node.next
    next_node.prev = prev_node
    prev_node.next = next_node

# add to start of linked list
def add_to_start(node_to_add: DoubleListNode, head: DoubleListNode):
    node_to_add.prev = head
    node_to_add.next = head.next
    # double link to the head 
    head.next.prev = node_to_add
    head.next = node_to_add

# remove from start of linked list
def remove_from_start(head: DoubleListNode, tail: DoubleListNode):
    if head.next == tail:
        return

    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next
    
# add to end of linked list
# NOTE: the true end of the list is the tail node
def add_to_end(node_to_add: DoubleListNode, tail: DoubleListNode):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    # double link to the tail 
    tail.prev.next = node_to_add
    tail.prev = node_to_add

# remove from end of linked list
# NOTE: the true end of the list is the tail node
def remove_from_end(head: DoubleListNode, tail: DoubleListNode):
    if head.next == tail:
        return
   
    # why is this node.prev.next pointing to tail?
    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head
