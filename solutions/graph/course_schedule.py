from typing import List


class Course:
    def __init__(self):
        self.indegree = 0
        self.subseq = []

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = [Course() for _ in range(numCourses)]
    for p in prerequisites:
        idf = p[0]
        pre = p[1]
        graph[idf].indegree+=1
        graph[pre].subseq.append(idf)

    queue = list()
    for i, C in enumerate(graph):
        if not C.indegree:
            queue.append(i)

    idx = 0
    while idx < len(queue):
        idf = queue[idx]
        vet = graph[idf]
        for j in vet.subseq:
            graph[j].indegree-=1
            if not graph[j].indegree:
                queue.append(j)
        idx+=1

    return queue if len(queue) < numCourses else []