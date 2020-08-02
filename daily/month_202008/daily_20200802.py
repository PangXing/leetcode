# coding:utf-8

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten_list(self, root):
        if not root:
            return []
        res = list()
        res.append(root.val)
        left = self.flatten_list(root.left)
        right = self.flatten_list(root.right)
        res.extend(left)
        res.extend(right)
        return res

    def flatten(self, root):
        if not root:
            return None
        l1 = self.flatten_list(root)
        p = root
        for i in range(1, len(l1)):
            p.right = TreeNode(l1[i])
            p.left = None
            p = p.right
        return root

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    res = solution.flatten(root)
    print res