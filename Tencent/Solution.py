# coding:utf-8

from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def printTree(self, root):
        if not root:
            return []
        res = list()
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            item = queue.popleft()

            if item:
                res.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        return res

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    res = solution.printTree(root)
    print res



