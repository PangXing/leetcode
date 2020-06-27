# coding:utf-8

'''
【145. 二叉树的后序遍历】
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    使用迭代法 后序遍历
    '''
    def postorderTraversal1(self, root):
        if not root:
            return []
        stack = list()
        stack.append(root)
        res = []
        while stack:
            r = stack.pop()
            res.append(r.val)
            if r.left:
                stack.append(r.left)
            if r.right:
                stack.append(r.right)
        return res[::-1]

    def postorderTraversal(self, root):
        if not root:
            return []
        stack = []
        output = []
        last_visited = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack[-1]
            if node.right == None or last_visited == node.right:
                stack.pop()
                output.append(node.val)
                last_visited = node
            else:
                root = node.right

        return output

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print solution.postorderTraversal(root)