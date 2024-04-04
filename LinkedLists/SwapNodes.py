"""
Swap nodes in pairs. Given a linked list
swap every pair of nodes. Example:
1->2->3->4->5->6
2->1->4->3->6->5

1. Starting with head at node A, we need B to point here.
    * We can accomplish this by doing head.next.next = head
2. However, if we change B.next, we lose access to rest of the list
    * Before applying change in 1, save pointer
        nextNode = head.next.next

head.next.next is used differently in steps 1 and 2.
It is changing head.next's next node. When it's after
the assignment, it is referring to head.next's next node.

1. We now have B pointing at A. We need to move on to the
next pair C, D.  

"""
