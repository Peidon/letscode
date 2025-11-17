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

        left_link = ListNode(0)
        left_link.next = ListNode(0)
        left_link.next.next = head
        while left_link and left > 0:
            left_link = left_link.next
            left -= 1
            right -= 1

        right_end = left_link.next
        if not right_end or not right_end.next:
            return head

        prior = right_end
        while right_end.next and right > 0:
            right -= 1
            reverse = right_end.next
            right_end.next = reverse.next
            reverse.next = prior
            prior = reverse
        left_link.next = prior

        if head_reverse:
            return left_link.next

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

