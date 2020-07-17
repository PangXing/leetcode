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

class Solution(object):
    def __init__(self):
        self._max_sum = float('-inf')
        self._single_sum = dict()

    def maxSingleSum(self, root):
        if not root:
            return 0
        if root in self._single_sum:
            return self._single_sum[root]

        left_max = self.maxSingleSum(root.left)
        right_max = self.maxSingleSum(root.right)
        tmp_max = max(left_max, right_max)
        if tmp_max > 0:
            res = root.val + tmp_max
        else:
            res = root.val
        self._single_sum[root] = res
        return res

    def maxPathSum(self, root):
        if not root:
            return 0
        self.maxPathSum(root.left)
        self.maxPathSum(root.right)

        left_max = self.maxSingleSum(root.left)
        right_max = self.maxSingleSum(root.right)
        tmp_max = max(root.val, root.val + left_max, root.val+ right_max, root.val + left_max + right_max)
        if tmp_max > self._max_sum:
            self._max_sum = tmp_max
        return self._max_sum

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print solution.maxPathSum(root)