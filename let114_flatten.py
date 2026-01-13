from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        p = root
        while p:

            while p.left:
                stack.append(p.left)
                p = p.left

            if p.right:
                p = p.right
            else:
                a = stack.pop()
                if a.right:
                    p.right = a.right
                a.right = p
                a.left = None
                p = a

        return

# pre-order
def build_tree(a: List[int]) -> Optional[TreeNode]:
    if not a:
        return None

    root = TreeNode(a[0])
    vec = [root]
    for x, v in enumerate(a[1:]):
        if v < 0:
            continue
        n = TreeNode(v)
        vec.append(n)
        k = x // 2
        if x & 1 > 0:
            vec[k].right = n
        else:
            vec[k].left = n

    return root

def travel(t: TreeNode) -> None:
    pass

if __name__ == '__main__':
    a = [1, 2, 5, 3, 4, -1, 6]
    t = build_tree(a)
    Solution().flatten(t)
