from typing import List


class Course:
    def __init__(self):
        self.indegree = 0
        self.subseq = []

def findOrder(nums: int, prerequisites: List[List[int]]) -> List[int]:
    """
    There are a total of `nums` courses labeled from 0 to `nums-1`,
    Given prerequisites, where prerequisites[i] = [a_, b_], b_ is the prerequisite of a_.
    Return the ordering of courses you should take to finish all courses.
    """

    # 1. parse the inputs to graph
    graph = [Course() for _ in range(nums)]

    for p in prerequisites:
        cur = p[0]
        pre = p[1]
        graph[cur].indegree+=1
        graph[pre].subseq.append(cur)

    # 2. initial the graph
    queue = list()
    for i, course in enumerate(graph):
        if not course.indegree:
            queue.append(i)

    # 3. topo sort
    for cur in queue:
        course = graph[cur]
        for j in course.subseq:
            graph[j].indegree -= 1
            if not graph[j].indegree:
                queue.append(j)

    return queue if len(queue) == nums else []