# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def recoverTree(self, root):
        if not root:
            return None
        if root.left and root.val <= root.left.val:
            tmp = root.val
            root.val = root.left.val
            root.left.val = tmp
            return root
        if root.right and root.val >= root.right.val:
            tmp = root.val
            root.val = root.right.val
            root.right.val = tmp
            return root
        self.recoverTree(root.left)
        self.recoverTree(root.right)
        return root

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root = solution.recoverTree(root)
    print root

