# coding:utf-8

import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec(object):

    def _serialize(self, root):
        if not root:
            return [None]
        res = list()
        res.append(root.val)
        res.extend(self._serialize(root.left))
        res.extend(self._serialize(root.right))
        return res

    def serialize(self, root):
        return json.dumps(self._serialize(root))

    def _deserialize(self, nodes):
        if nodes:
            return None
        x = nodes.pop(0)
        if x is None:
            return None
        root = TreeNode(x)
        root.left = self._deserialize(nodes)
        root.right = self._deserialize(nodes)
        return root

    def deserialize(self, data):
        return self._deserialize(json.loads(data))

if __name__ == '__main__':
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    data = codec.serialize(root)
    print data
    root1 = codec.deserialize(data)
    print root1


