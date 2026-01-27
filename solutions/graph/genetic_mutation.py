from collections import deque
from typing import List


def adjacent(a: str, b: str) -> bool:
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c+=1
    return c==1

def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    queue = deque([startGene])
    bank_mark = set()
    mutation = 0

    while queue:
        breadth = len(queue)
        for i in range(breadth):
            node = queue.popleft()
            if node==endGene:
                return mutation

            for b in bank:
                if adjacent(b, node) and b not in bank_mark:
                    queue.append(b)
                    bank_mark.add(b)
        mutation+=1
    return -1