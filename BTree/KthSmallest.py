# coding:utf-8
'''
【230. 二叉搜索树中第K小的元素】
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    二叉搜索树的树 中序遍历
    '''
    def findnode(self, r, k):
        if not r or self._cnt > k:
            return None
        left_r = self.findnode(r.left, k)
        if left_r:
            return left_r
        self._cnt += 1
        if self._cnt == k:
            return r
        right_r = self.findnode(r.right, k)
        return right_r

    def kthsmallest(self, root, k):
        self._cnt = 0
        return self.findnode(root, k).val

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print solution.kthsmallest(root, 2)


