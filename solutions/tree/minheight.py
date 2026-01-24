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

    node = [vertex() for _ in range(n)]

    for out, ind in edges:
        node[ind].append(out)
        node[out].append(ind)

    # leave index
    leaves = [x for x in range(n) if node[x].in_degree == 1]

    while n > 2:
        n -= len(leaves)
        leaves_que = []
        for leaf in leaves:

            c_idx = node[leaf].pop_conjoin()
            # c_idx: conjoin vertex index
            node[c_idx].in_degree -= 1
            if node[c_idx].in_degree == 1:
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

            for adj_idx in adj[leaf]:

                in_degree[adj_idx] -= 1
                if in_degree[adj_idx] == 1:
                    leaves_que.append(adj_idx)

        leaves = leaves_que
        print(leaves)

    return leaves


if __name__ == '__main__':
    findMinHeight(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
