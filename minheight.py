class vertex:
    def __init__(self):
        self.conjoin = []
        self.in_degree = 0

    def append(self, conjoin: int):
        self.conjoin.append(conjoin)
        self.in_degree += 1

    def pop_conjoin(self) -> int:
        return self.conjoin.pop()


def findMinHeight(n: int, edges):
    if not edges:
        return [0]

    adj = [vertex() for _ in range(n)]

    for out, ind in edges:
        adj[ind].append(out)
        adj[out].append(ind)

    leaves = [x for x in range(n) if adj[x].in_degree == 1]

    while n > 2:
        n -= len(leaves)
        leaves_que = []
        for leaf in leaves:

            c_idx = adj[leaf].pop_conjoin()
            # c_idx: conjoin vertex index
            adj[c_idx].in_degree -= 1
            if adj[c_idx].in_degree == 1:
                leaves_que.append(c_idx)

        leaves = leaves_que
        print(leaves)

    return leaves


def findMinHeightTrees(n: int, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    adj = [[] for __ in range(n)]

    if not edges:
        return [0]

    in_degree = [0] * n

    for out, ind in edges:
        adj[ind].append(out)
        adj[out].append(ind)
        in_degree[ind] += 1
        in_degree[out] += 1

    leaves = [x for x in range(n) if in_degree[x] == 1]

    while n > 2:
        n -= len(leaves)
        leaves_que = []
        for leaf in leaves:

            for vertex in adj[leaf]:

                in_degree[vertex] -= 1
                if in_degree[vertex] == 1:
                    leaves_que.append(vertex)

        leaves = leaves_que
        print(leaves)

    return leaves


if __name__ == '__main__':
    findMinHeight(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
