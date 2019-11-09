# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        
        path = []
        ans = []
        self.getPath(root, path, sum, ans)
        return ans

    def getPath(self, root, path, sum, ans):
        path.append(root.val)
        if not root.left and not root.right:
            if root.val == sum:
                ans.append(path)
        
        if not root.left:
            self.getPath(root.left, path, sum - root.val, ans)
        if not root.right:
            self.getPaht(root.right, path, sum - root.val, ans)

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def stringToInt(input):
    return int(input)

def int2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            root = stringToTreeNode(line)
            line = lines.next()
            sum = stringToInt(line)
            
            ret = Solution().pathSum(root, sum)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()