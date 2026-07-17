from collections import deque
from typing import List


def adjacent(a: str, b: str) -> bool:
    """
    check if a can be mutated to b use just one mutation.
    """
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c+=1
    return c==1

def minMutation(start_gene: str, end_gene: str, bank: List[str]) -> int:
    queue = deque([start_gene])
    bank_mark = set()
    mutation = 0

    # start bfs
    while queue:
        breadth = len(queue)
        for i in range(breadth):
            node = queue.popleft()
            if node==end_gene:
                return mutation

            for b in bank:
                if adjacent(b, node) and b not in bank_mark:
                    queue.append(b)
                    bank_mark.add(b)
        mutation+=1
    return -1