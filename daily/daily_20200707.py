# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
            return False

        if (not root.left) and (not root.right):
            if sum == root.val:
                return True
            else:
                return False
        else:
            sum -= root.val
            left_res = self.hasPathSum(root.left, sum)
            right_res = self.hasPathSum(root.right, sum)
            return left_res or right_res

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print solution.hasPathSum(root, 22)