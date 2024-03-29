# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


from collections import deque


def levelOrder01(root: Node):
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    q = deque()

    ans = []
    if root:
        q.append(root)

    while q:
        levelsum = len(q)
        levelnode = []

        for _ in range(levelsum):
            node = q.popleft()
            levelnode.append(node.val)
            for child in node.children:
                q.append(child)
        ans.append(levelnode)
    return ans


def levelOrder00(root):
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

    while queue:
        level = []
        i = len(queue)
        while i > 0:
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i -= 1
        ret.append(level)
    return ret


def zigzagLevelOrder(root):
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

    level_count = 0
    while queue:
        level = []
        i = len(queue)

        level_count += 1
        while i > 0:
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i -= 1
        if level_count % 2:
            ret.append(level)
        else:
            ret.append(level[::-1])

    return ret


class Solution(object):
    pass
