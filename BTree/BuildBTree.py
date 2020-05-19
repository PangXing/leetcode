# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        left = inorder[:index]
        right = inorder[index+1:]
        root.left = self.buildTree(preorder[1:1+len(left)], left)
        root.right = self.buildTree(preorder[-len(right):], right)
        return root


