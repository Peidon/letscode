
from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites: return True

        indegree = [0] * numCourses # indegree

        adj = [[] for _ in range(numCourses)] # adjacency set
        edge = 0
        for cur, pre in prerequisites:
            indegree[cur] += 1
            adj[pre].append(cur)
            edge += 1
        queue = deque()
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
        
        if not queue:
            return False

        while queue:
            vertex = queue.popleft()
            while adj[vertex]:
                adjacency = adj[vertex].pop()
                indegree[adjacency] -= 1
                edge -= 1
                if not indegree[adjacency]: queue.append(adjacency)

        return not edge