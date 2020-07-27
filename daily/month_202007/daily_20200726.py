# coding:utf-8
'''
【329. 矩阵中的最长递增路径】
给定一个整数矩阵，找出最长递增路径的长度。
对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:
输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。

示例 2:
输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
'''

class Solution(object):
    '''
    记忆化深度优先搜索
    '''
    def __init__(self):
        self.dp = dict()

    def findLongest(self, matrix, row, col):
        key = (row, col)
        if key in self.dp:
            return self.dp[key]
        val = matrix[row][col]
        rows = len(matrix)
        cols = len(matrix[0])
        right = col + 1
        left = col - 1
        up = row - 1
        down = row + 1
        longest = 1
        if right < cols and matrix[row][right] < val:
            tmp = self.findLongest(matrix, row, right) + 1
            if tmp > longest:
                longest = tmp
        if left > -1 and matrix[row][left] < val:
            tmp = self.findLongest(matrix, row, left) + 1
            if tmp > longest:
                longest = tmp
        if down < rows and matrix[down][col] < val:
            tmp = self.findLongest(matrix, down, col) + 1
            if tmp > longest:
                longest = tmp
        if up > -1 and matrix[up][col] < val:
            tmp = self.findLongest(matrix, up, col) + 1
            if tmp > longest:
                longest = tmp
        self.dp[key] = longest
        return longest

    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        longest_num = 0
        for row in range(rows):
            for col in range(cols):
                tmp = self.findLongest(matrix, row, col)
                if tmp > longest_num:
                    longest_num = tmp
        return longest_num

if __name__ == '__main__':
    solution = Solution()
    nums = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    print solution.longestIncreasingPath(nums)