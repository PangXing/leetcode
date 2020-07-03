# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self._midorder = list()

    def traversalIn(self, root):
        '''中序遍历'''
        if not root:
            return
        self.traversalIn(root.left)
        self._midorder.append(root.val)
        self.traversalIn(root.right)

    def rebuildBST(self, l1):
        if not l1:
            return None
        mid = (len(l1) -1)/2
        root = TreeNode(l1[mid])
        root.left = self.rebuildBST(l1[0:mid])
        root.right = self.rebuildBST(l1[mid+1:])
        return root

    def balanceBST(self, root):
        if not root:
            return root
        self._midorder = list()
        self._midorder.sort()
        root = self.rebuildBST(self._midorder)
        return root

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    res = solution.balanceBST(root)
    print res

