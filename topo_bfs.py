from collections import deque


class Vertex:
    def __init__(self):
        self.adj = []  # vertex list
        self.in_degree = 0


class graph:
    def __init__(self, n):
        self.node_list = [Vertex() for _ in range(n)]

    def build(self, prerequisites):
        for cur, pre in prerequisites:
            p = self.node_list[pre]
            c = self.node_list[cur]
            p.adj.append(c)
            c.in_degree += 1


def canFinish(num_courses, prerequisites):
    """
    :type num_courses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if not prerequisites: return True

    g = graph(num_courses)
    g.build(prerequisites)

    adj_list = g.node_list # adjacency list

    queue = deque()
    for v in adj_list:
        if not v.in_degree:
            queue.append(v)

    if not queue:
        return False

    while queue:
        v = queue.popleft()
        num_courses -= 1
        while v.adj:
            adjacency = v.adj.pop()
            adjacency.in_degree -= 1
            if not adjacency.in_degree:
                queue.append(adjacency)

    return not num_courses


if __name__ == '__main__':
    print(canFinish(3, [[1, 0], [1, 2]]))
