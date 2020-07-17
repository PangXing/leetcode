# coding:utf-8

from collections import deque
import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec(object):
    def serialize(self, root):
        if not root:
            return []
        data = [root.val]
        data.append(self.serialize(root.left))
        data.append(self.serialize(root.right))
        return data

    def deserialize(self, data):
        if not data:
            return None
        root = TreeNode(data[0])
        if data[1]:
            root.left = self.deserialize(data[1])
        else:
            root.left = None
        if data[2]:
            root.right = self.deserialize(data[2])
        else:
            root.right = None
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    codec = Codec()
    s = codec.serialize(root)
    print s
    res = codec.deserialize(s)
    print res




