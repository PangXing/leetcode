# coding:utf-8
'''
【437. 路径总和 III】
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
返回 3。和等于 8 的路径有:
1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def count(self, root, sum):
        if not root:
            return 0
        cnt = 1 if root.val == sum else 0
        cnt_left = self.count(root.left,  sum-root.val)
        cnt_right = self.count(root.right, sum-root.val)
        return cnt + cnt_left + cnt_right

    def pathSum(self, root, sum):
        if not root:
            return 0
        cnt = self.count(root, sum)
        left_cnt = self.pathSum(root.left, sum)
        right_cnt = self.pathSum(root.right, sum)
        return cnt +left_cnt +right_cnt

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.left = TreeNode(1)
    root.right.right = TreeNode(11)
    print solution.pathSum(root, 8)
