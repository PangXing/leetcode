# coding:utf-8

'''
【322. 零钱兑换】
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1
 
说明:
你可以认为每种硬币的数量是无限的。
'''

class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        if not coins or amount < 0:
            return -1
        dp = [0]
        for i in range(1, amount+1):
            min_num = float('inf')
            for k in coins:
                if i == k:
                    min_num = 1
                elif i > k:
                    min_num = min(min_num, dp[i-k] + 1)
            dp.append(min_num)
        nums = dp[amount]
        if nums == float('inf'):
            nums = -1
        return nums

if __name__ == '__main__':
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    coins = [2]
    amount = 3
    print solution.coinChange(coins, amount)
