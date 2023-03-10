from collections import deque


def canFinish(num_courses, prerequisites):
    """
    :type num_courses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if not prerequisites: return True

    in_degree = [0] * num_courses  # in_degree
    adj = [[] for _ in range(num_courses)]  # adjacency set

    for cur, pre in prerequisites:
        in_degree[cur] += 1
        adj[pre].append(cur)
    queue = deque()
    for i in range(num_courses):
        if not in_degree[i]:
            queue.append(i)

    if not queue:
        return False

    while queue:
        vertex = queue.popleft()
        num_courses -= 1
        while adj[vertex]:
            adjacency = adj[vertex].pop()
            in_degree[adjacency] -= 1
            if not in_degree[adjacency]: queue.append(adjacency)

    return not num_courses


print(canFinish(3, [[1, 0], [1, 2]]))
