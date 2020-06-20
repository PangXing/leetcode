# coding:utf-8

'''
【450. 删除二叉搜索树中的节点】

给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findleftval(self, root):
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root, key):
        if not root:
            return None
        if root.val == key:
            if root.left and root.right:
                val = self.findleftval(root.right)
                root.val = val
                root.right = self.deleteNode(root.right, val)
            elif root.left:
                root.val = root.left.val
                root.right = root.left.right
                root.left = root.left.left
            elif root.right:
                root.val = root.right.val
                root.left = root.right.left
                root.right = root.right.right
            else:
                root = None
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    tmp = solution.deleteNode(root, 3)
    print tmp

