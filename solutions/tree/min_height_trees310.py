from typing import List


class Vertex:
    def __init__(self):
        self.conjoin = set()
        self.in_degree = 0

    def append(self, conjoin: int):
        self.conjoin.add(conjoin)
        self.in_degree += 1

    def pop_conjoin(self) -> int:
        return self.conjoin.pop()

    def remove_conjoin(self, x):
        self.conjoin.remove(x)


class Graph:
    def __init__(self, n: int):
        self.M = [Vertex() for _ in range(n)]

    def conjoin(self, a: int, b: int):
        self.M[a].append(b)
        self.M[b].append(a)

    def is_leaf(self, x):
        return self.M[x].in_degree == 1

    def detach(self, x) -> List[int]:
        v = self.M[x]
        detached = []
        while v.conjoin:
            c_idx = v.pop_conjoin()
            self.M[c_idx].in_degree-=1
            self.M[c_idx].remove_conjoin(x)
            detached.append(c_idx)
        return detached



def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    """
    Let's think about it from the opposite, how can I increase the minimum height of tree by adding one node.
    Obviously, this node must be a leaf.
    So, how to reduce the height, the answer is removing the leaves.
    """

    if not edges:
        # no edges that indicates every node is isolated
        return [0]

    # adjacent matrix
    graph = Graph(n)

    for out, ind in edges:
        graph.conjoin(out, ind)

    # leave index
    leaves = [x for x in range(n) if graph.is_leaf(x)]

    while n > 2:
        n -= len(leaves)
        leaves_que = []
        for leaf in leaves:

            detached = graph.detach(leaf)
            for d in detached:
                if graph.is_leaf(d):
                    leaves_que.append(d)

        leaves = leaves_que

    return leaves


if __name__ == '__main__':
    ans = findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    assert ans == [3,4]

    ans = findMinHeightTrees(7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]])
    assert ans == [1,2]
