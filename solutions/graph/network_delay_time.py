class Edge:
    def __init__(self, dest: int, duration: int):
        self.duration = duration
        self.destination = dest

    def __lt__(self, other):
        return self.duration < other.duration

class Node:
    def __init__(self, label: int):
        self.time = 0
        self.label = label
        self.edges = []
        self.path = set()

    def add_edge(self, u: int, v: int):
        self.edges.append(Edge(u, v))

class Graph:

    def __init__(self, times: list[list[int]], n: int):
        nodes = [Node(x+1) for x in range(n)]
        for u, v, w in times:
            # because index is less one than label
            nodes[u - 1].add_edge(v, w)
        self.node_list = nodes

    def get_node(self, k: int) -> Node:
        return self.node_list[k - 1]

import heapq
from collections import deque

class SpanTree:

    def __init__(self, g: Graph):
        self.nodes = set()  # reached nodes
        self.edges = []     # edges whose destination don't exist in nodes
        self.graph = g      # hold the reference of graph

    def reach_node(self, node: Node) -> bool:
        if node.label in self.nodes:
            return False
        self.nodes.add(node.label)
        for edge in node.edges:
            edge.duration += node.time
            self.add_edge(edge)
        return True

    def add_edge(self, edge: Edge):
        heapq.heappush(self.edges, edge)

    def pop_edge(self) -> Edge:
        return heapq.heappop(self.edges)

    def extend_from_k(self, k: int):
        que = deque()
        que.append(self.graph.get_node(k))
        while que:
            node = que.popleft()
            if not self.reach_node(node):
                continue
            while self.edges:
                edge = self.pop_edge()
                neighbor = self.graph.get_node(edge.destination)
                if not edge.destination in self.nodes:
                    neighbor.time = edge.duration
                    que.append(neighbor)
                    break
                neighbor.time = min(neighbor.time, edge.duration)


    def get_delay_time(self):
        return max([node.time for node in self.graph.node_list])


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = Graph(times, n)
    tree = SpanTree(graph)
    tree.extend_from_k(k)
    if len(tree.nodes) < n:
        return -1
    return tree.get_delay_time()


if __name__ == '__main__':
    outcome = networkDelayTime([[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]], 5, 5)
    print(outcome) # should be 31
    outcome2 = networkDelayTime([[2,4,10],[5,2,38],[3,4,33],[4,2,76],[3,2,64],[1,5,54],[1,4,98],[2,3,61],[2,1,0],[3,5,77],[5,1,34],[3,1,79],[5,3,2],[1,2,59],[4,3,46],[5,4,44],[2,5,89],[4,5,21],[1,3,86],[4,1,95]], 5, 1)
    print(outcome2) # should be 69