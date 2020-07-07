# coding:utf-8

'''
【63. 不同路径 II】
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        row_len = len(obstacleGrid)
        col_len = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[row_len-1][col_len-1]:
            return 0
        dp = list()
        for row in range(row_len):
            dp.append(list())
            for col in range(col_len):
                if row == 0 and col == 0:
                    dp[row].append(1)
                elif obstacleGrid[row][col]:
                    dp[row].append(0)
                elif row == 0:
                    dp[row].append(dp[row][col-1])
                elif col == 0:
                    dp[row].append(dp[row-1][col])
                else:
                    dp[row].append(dp[row][col-1] + dp[row-1][col])
        return dp[row_len-1][col_len-1]

if __name__ == '__main__':
    solution = Solution()
    obstacleGrid = [[0,0,0],
                    [0,1,0],
                    [0,0,0]]
    print solution.uniquePathsWithObstacles(obstacleGrid)

