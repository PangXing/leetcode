# coding:utf-8
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = list()
        flag = True
        visited = deque()
        visited.append(root)
        while visited:
            item = list()
            for i in range(len(visited)):
                r = visited.popleft()
                item.append(r.val)
                if r.left:
                    visited.append(r.left)
                if r.right:
                    visited.append(r.right)
            if flag:
                res.append(item)
            else:
                res.append(item[::-1])
            flag = (not flag)
        return res

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print solution.zigzagLevelOrder(root)


