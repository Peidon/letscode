from collections import deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        minhei = self.heightCalculate(0, n, adj)
        heightList = [minhei]
        ans = []
        for root in range(1,n):
            tmp = self.heightCalculate(root, n, adj)
            heightList.append(tmp)
        print(heightList)
        return ans
        
    def heightCalculate(self, root, n, adj):
        height = 0
        visited = [0] * n
        que = deque([root])
        visited[root] = 1
        while que:
            length = len(que)
            height += 1
            while length > 0:
                node = que.popleft()
                for neibor in adj[node]:
                    if not visited[neibor]:
                        que.append(neibor)
                        visited[neibor] = 1
                length -= 1
            
        return height


Solution().findMinHeightTrees(4,[[1,0],[1,2],[1,3]])