# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if root.val in [p, q]:
            return root.val
        left_val = self.lowestCommonAncestor(root.left, p, q)
        right_val = self.lowestCommonAncestor(root.right, p, q)
        if left_val and right_val:
            return root.val
        elif left_val:
            return left_val
        else:
            return right_val

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    print solution.lowestCommonAncestor(root, 5, 1)