# coding:utf-8

'''
【256 粉刷房子】
这里有n个房子在一列直线上，现在我们需要给房屋染色，分别有红色蓝色和绿色。每个房屋染不同的颜色费用也不同，你需要设计一种染色方案使得相邻的房屋颜色不同，并且费用最小，返回最小的费用。
费用通过一个nx3 的矩阵给出，比如cost[0][0]表示房屋0染红色的费用，cost[1][2]表示房屋1染绿色的费用。

样例
样例 1:
输入: [[14,2,11],[11,14,5],[14,3,10]]
输出: 10
解释: 第一个屋子染蓝色，第二个染绿色，第三个染蓝色，最小花费：2 + 5 + 3 = 10.

样例 2:
输入: [[1,2,3],[1,4,6]]
输出: 3
注意事项
所有费用都是正整数

'''
class Solution(object):
    def minCost(self, costs):
        '''
        状态：DP[i][0] 前i个房子使用红色的最低费用
        '''
        if not costs:
            return 0
        n = len(costs)
        dp = list()
        dp.append([0, 0, 0])
        for i in range(1, n+1):
            dp.append(list())
            dp[i].append(min(dp[i-1][1] + costs[i-1][0], dp[i-1][2] + costs[i-1][0]))
            dp[i].append(min(dp[i-1][0] + costs[i-1][1], dp[i-1][2] + costs[i-1][1]))
            dp[i].append(min(dp[i-1][0] + costs[i-1][2], dp[i-1][1] + costs[i-1][2]))
        return min(dp[n])

if __name__ == '__main__':
    solution = Solution()
    costs = [[14,2,11],[11,14,5],[14,3,10]]
    print solution.minCost(costs)