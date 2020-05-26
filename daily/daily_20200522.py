# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def print_tree(self):
        print '%s' %self.val
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return  None
        x = preorder[0]
        index = inorder.index(x)
        node = TreeNode(x)
        node.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        node.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return node

if __name__ == '__main__':
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree = solution.buildTree(preorder, inorder)
    tree.print_tree()
