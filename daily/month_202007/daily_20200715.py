# coding:utf-8

'''
96. 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Solution(object):
    def __init__(self):
        self.dp = {}
        self.dp[0] = 0
        self.dp[1] = 1
        self.dp[2] = 2
        self.dp[3] = 5

    def buildBST(self, l1):
        n = len(l1)
        if n in self.dp:
            return self.dp[n]
        cnt = 0
        for i in range(n):
            left_cnt = 1
            if i < n -1:
                left = l1[i+1:]
                left_cnt = self.buildBST(left)
            right_cnt = 1
            if i > 1:
                right = l1[:i]
                right_cnt = self.buildBST(right)
            cnt += (left_cnt * right_cnt)
        self.dp[n] = cnt
        return cnt

    def numTrees1(self, num):
        l1 = [i for i in range(1, num+1)]
        self.buildBST(l1)
        return self.dp[num]

    def numTrees(self, n):
        dp = list()
        dp.append(1)
        dp.append(1)
        for i in range(2, n+1):
            dp.append(0)
            for j in range(1, i+1):
                dp[i] += (dp[j-1] * dp[i-j])
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    num = 6
    print solution.numTrees(num)