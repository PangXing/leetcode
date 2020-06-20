# coding:utf-8

'''
【98. 验证二叉搜索树】
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBST(self, root, r_min, r_max):
        if not root: return True
        if r_min and root.val <= r_min.val: return False
        if r_max and root.val >= r_max.val: return False
        left = self.isBST(root.left, r_min, root)
        right = self.isBST(root.right, root, r_max)
        return True if left and right else False

    def isValidBST(self, root):
        return self.isBST(root, None, None)

if __name__ == '__main__':
    solution = Solution()
    root =  TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print solution.isValidBST(root)
