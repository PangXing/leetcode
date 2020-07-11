# coding:utf-8

'''
【315. 计算右侧小于当前元素的个数】
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:
输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.cnt = 0
        self.left_cnt = 0

class BSTree(object):
    '''
    使用二叉搜索树也可以完成插入并统计的功能，从右往左构建二叉树。
    '''
    def __init__(self):
        self._res = list()

    def insert(self, root, x, cnt):
        if not root:
            newNode = TreeNode(x)
            newNode.cnt = cnt
            self._res.append(cnt)
            return newNode
        if root.val == x:
            cnt = cnt + root.left_cnt
            root.right = self.insert(root.right, x, cnt)
        elif root.val > x:
            root.left_cnt += 1
            root.left = self.insert(root.left, x, cnt)
        else:
            cnt = cnt + 1 + root.left_cnt
            root.right = self.insert(root.right, x, cnt)
        return root

    def get_counte(self):
        return self._res[::-1]


class Solution(object):
    def countSmaller(self, nums):
        if not nums:
            return []
        size = len(nums)
        if size == 1:
            return [0]
        tree = BSTree()
        root = None
        for i in nums[::-1]:
            root = tree.insert(root, i, 0)
        return tree.get_counte()

if __name__ == '__main__':
    solution = Solution()
    nums = [5, 2, 6, 1]
#    nums = [0, 1, 2]
#    nums = [2, 0, 1]
    nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
    print solution.countSmaller(nums)
    [10, 27, 10, 35, 12, 22, 28, 8, 19, 2, 12, 2, 9, 6, 12, 5, 17, 9, 19, 12, 14, 6, 12, 5, 12, 3, 0, 10, 0, 7, 8, 4, 0,
     0, 4, 3, 2, 0, 1, 0]
