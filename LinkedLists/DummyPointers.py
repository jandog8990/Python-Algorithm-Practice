def get_sum(head: ListNode):
    ans = 0
    dummy = head
    while dummy:
        ans += dummy.val
        dummy = dummy.next

    return ans
