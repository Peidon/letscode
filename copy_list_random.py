from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, nxt: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = nxt
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # step 1, replicate
        it = head

        while it:
            copy = Node(it.val)

            nxt = it.next
            it.next = copy
            copy.next = nxt
            it = nxt

        # step 2, copy random_index
        it = head
        while it:
            if it.random:
                it.next.random = it.random.next
            it = it.next.next

        # step 3, break down
        it = head
        copy = head.next
        p = Node(0)
        while it:
            p.next = it.next
            nxt = p.next.next
            if nxt:
                p.next.next = nxt.next
            it.next = nxt
            it = nxt

        return copy

if __name__ == '__main__':
    vec = [[7,-1],[13,0],[11,4],[10,2],[1,0]]
    head = Node(0)
    p = head
    for v in vec:
        p.next = Node(v[0])
        p = p.next

    j = head.next
    for v in vec:
        r = v[1]
        if r >= 0:
            q = head
            for i in range(r):
                q = q.next
            j.random = q

        j = j.next

    result = Solution().copyRandomList(head.next)
    a = []
    pseudo = result
    while pseudo:
        a.append(pseudo.val)
        pseudo = pseudo.next
    print(a)
