# coding:utf-8

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildBST(self, l1):
        n = len(l1)
        if n == 1:
            return [TreeNode(l1[0])]
        res = list()
        for i in range(n):
            if i == 0:
                left = [None]
            else:
                left = self.buildBST(l1[0:i])
            if i == n-1:
                right = [None]
            else:
                right = self.buildBST(l1[i+1:])
            for j in left:
                for k in right:
                    res.append(TreeNode(l1[i], j, k))
        return res

    def generateTrees(self, n):
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]
        l1 = range(1, n+1)
        return self.buildBST(l1)




if __name__ == '__main__':
    solution = Solution()
    n = 3
    res = solution.generateTrees(n)
    print res