# coding:utf-8

'''
【62. 不同路径】
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径
例如，上图是一个7 x 3 的网格。有多少可能的路径？

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28

提示：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9
'''

class Soluton(object):
    def uniquePaths(self, m, n):
        dp = list()
        for row in range(m):
            if row == 0:
                dp.append([1 for i in range(n)])
            else:
                dp.append(list())
                for col in range(n):
                    if col == 0:
                        dp[row].append(1)
                    else:
                        dp[row].append(dp[row-1][col] + dp[row][col-1])
        return dp[m-1][n-1]

if __name__ == '__main__':
    solution = Soluton()
    print solution.uniquePaths(7, 3)