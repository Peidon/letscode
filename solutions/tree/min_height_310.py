class Vertex:
    def __init__(self):
        self.conjoin = []
        self.in_degree = 0

    def append(self, conjoin: int):
        self.conjoin.append(conjoin)
        self.in_degree += 1

    def pop_conjoin(self) -> int:
        return self.conjoin.pop()


class Graph:
    def __init__(self, n: int):
        self.M = [Vertex() for _ in range(n)]

    def conjoin(self, a: int, b: int):
        self.M[a].append(b)
        self.M[b].append(a)

    def is_leaf(self, x):
        return self.M[x].in_degree == 1

    def detach(self, x):
        v = self.M[x]
        while v.conjoin:
            c_idx = v.pop_conjoin()
            self.M[c_idx].in_degree-=1



def findMinHeight(n: int, edges):
    if not edges:
        return [0]

    # adjacent matrix
    graph = [Vertex() for _ in range(n)]

    for out, ind in edges:
        graph[ind].append(out)
        graph[out].append(ind)

    # leave index
    leaves = [x for x in range(n) if graph[x].in_degree == 1]

    while n > 2:
        n -= len(leaves)
        leaves_que = []
        for leaf in leaves:

            c_idx = graph[leaf].pop_conjoin()
            # c_idx: conjoin vertex index
            graph[c_idx].in_degree -= 1
            if graph[c_idx].in_degree == 1:
                leaves_que.append(c_idx)

        leaves = leaves_que
        print(leaves)

    return leaves


if __name__ == '__main__':
    findMinHeight(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
