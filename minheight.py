class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]

        if not edges: return [0]
        indgree = [0] * n

        for out, ind in edges:
            adj[ind].append(out)
            adj[out].append(ind)
            indgree[ind] += 1
            indgree[out] += 1
        leaves = []
        for i in range(n):
            if indgree[i] == 1:
                leaves.append(i)
        while(n > 2):
            n -= len(leaves)
            leaves_que = []
            for leaf in leaves:
                for node in adj[leaf]:
                    indgree[node] -= 1
                    if indgree[node] == 1:
                        leaves_que.append(node)
            leaves = leaves_que
            print(leaves)
        
        return leaves

Solution().findMinHeightTrees(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])