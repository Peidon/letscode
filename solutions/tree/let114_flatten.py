from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    For every tree node, move left subtree to right, and move right subtree to
    the [rightmost node] of the left subtree.
    """
    curr = root

    while curr:

        if curr.left:

            # Find the [rightmost node] of the left subtree.
            p = curr.left
            while p.right:
                p = p.right

            # move right subtree to the [rightmost] of the left subtree.
            p.right = curr.right

            # move left subtree to the right of current node
            curr.right = curr.left

            # remove the original reference to the left subtree
            curr.left = None

        curr = curr.right

    return

# pre-order
def build_tree(a: List[int]) -> Optional[TreeNode]:
    if len(a) == 0:
        return None

    root = TreeNode(a[0])
    vec = [root]
    for x, num in enumerate(a[1:]):
        if num < 0:
            continue
        n = TreeNode(num)
        vec.append(n)
        k = x // 2
        if x & 1 > 0:
            vec[k].right = n
        else:
            vec[k].left = n

    return root

def visit(root: TreeNode):
    if not root:
        return
    print(root.val)
    visit(root.left)
    visit(root.right)


if __name__ == '__main__':
    v = [1, 2, 5, 3, 4, -1, 6]
    t = build_tree(v)
    flatten(t)
    visit(t)

