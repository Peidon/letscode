# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ret = []
        queue = deque()

        if root:
            queue.append(root)
        else:
            return ret

        levelcount = 0
        while queue:
            level = []
            i = len(queue)

            levelcount += 1
            while(i > 0):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i -= 1
            if levelcount % 2: ret.append(level)
            else: ret.append(level[::-1])

        return ret