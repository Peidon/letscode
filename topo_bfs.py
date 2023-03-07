from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites: return True

        in_degree = [0] * numCourses  # in_degree
        adj = [[] for _ in range(numCourses)]  # adjacency set

        for cur, pre in prerequisites:
            in_degree[cur] += 1
            adj[pre].append(cur)
        queue = deque()
        for i in range(numCourses):
            if not in_degree[i]:
                queue.append(i)

        if not queue:
            return False

        while queue:
            vertex = queue.popleft()
            numCourses -= 1
            while adj[vertex]:
                adjacency = adj[vertex].pop()
                in_degree[adjacency] -= 1
                if not in_degree[adjacency]: queue.append(adjacency)

        return not numCourses


print(Solution().canFinish(3, [[1, 0], [1, 2]]))
