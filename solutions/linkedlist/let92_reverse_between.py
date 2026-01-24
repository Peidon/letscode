from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        head_reverse = left <= 1

        dummy = ListNode()
        dummy.next = ListNode()
        dummy.next.next = head
        while dummy and left > 0:
            dummy = dummy.next
            left -= 1
            right -= 1

        begin = dummy.next
        if not begin or not begin.next:
            return head

        prior = begin
        while begin.next and right > 0:
            right -= 1
            reverse = begin.next
            begin.next = reverse.next
            reverse.next = prior
            prior = reverse
        dummy.next = prior

        if head_reverse:
            return dummy.next

        return head

if __name__ == '__main__':
    test_dada = [3,4]
    head = ListNode(val=test_dada[0])
    p = head
    for item in test_dada[1:]:
        p.next = ListNode(val=item)
        p = p.next

    s = Solution()
    a = s.reverseBetween(head, 1, 2)
    while a:
        print(a.val)
        a = a.next

