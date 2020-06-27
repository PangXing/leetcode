# coding:utf-8

'''
【144. 二叉树的前序遍历】
给定一个二叉树，返回它的 前序 遍历。
 示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal1(self, root):
        if not root:
            return []
        output = []
        stack = []
        stack.append(root)
        while stack:
            r = stack.pop()
            output.append(r.val)
            if r.right:
                stack.append(r.right)
            if r.left:
                stack.append(r.left)
        return output

    def preorderTraversal(self, root):
        if not root:
            return []
        output = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                output.append(root.val)
                root = root.left
            root = stack.pop()
            root = root.right
        return output

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print solution.preorderTraversal(root)