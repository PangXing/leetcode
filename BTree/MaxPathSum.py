# coding:utf-8

'''
【124. 二叉树中的最大路径和】
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:
输入: [1,2,3]

       1
      / \
     2   3

输出: 6

示例 2:
输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def __init__(self):
        self.max_sum = 0

    def buildMaxTree(self, root):
        if not root:
            return 0
        root.leftmax = self.buildMaxTree(root.left)
        root.rightmax = self.buildMaxTree(root.right)
        maxval = max(root.val, root.val + root.leftmax, root.val + root.rightmax)
        return maxval

    def subPathSum(self, root, psum):
        if psum > self.max_sum:
            self.max_sum = psum

        if not root:
            return
        if psum <= 0:
            psum_left = root.rightmax + root.val if root.rightmax > 0 else root.val
            psum_right = root.leftmax + root.val if root.leftmax > 0 else root.val
        else:
            psum_left = max(psum, root.rightmax) + root.val
            psum_right = max(psum, root.leftmax) + root.val

        self.subPathSum(root.left, psum_left)
        self.subPathSum(root.right,  psum_right)

    def maxPathSum(self, root):
        if not root:
            return 0
        self.buildMaxTree(root)

        psum = root.val
        self.max_sum = psum
        self.subPathSum(root.left, root.rightmax + psum if root.rightmax > 0 else psum)
        self.subPathSum(root.right, root.leftmax + psum if root.leftmax > 0 else psum)
        return self.max_sum


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_gain(node):
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain

            # update max_sum if it's better to start a new path
            self.max_sum = max(self.max_sum, price_newpath)

            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)

        self.max_sum = float('-inf')
        max_gain(root)
        return self.max_sum


if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    print solution.maxPathSum(root)
