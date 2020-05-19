# coding:utf-8

'''
【题目】0-1背包问题，可装重量为W的背包和N个物品, 其中第1个物品的重量为wt[i] 价值为val[i] 现在你的背包物品最多价值？
【分类】动态规划
'''
class Solution(object):
    def find_max_val(self, wmax, wts, vals):
        '''
        【dp数组】前i个物品在 重量为w时 最大价值
        【选择】是否放入第i个物品
        【base】第1个物品的初始化

        '''
        dp = list()
        for i in range(0, len(wts)):
            item = list()
            for w in range(0, wmax+1):
                item.append(0)
            dp.append(item)
        #BASE
        for w in range(0, wmax+1):
            if wts[0] <= w:
                dp[0][w] = vals[0]

        for i in range(1, len(wts)):
            for w in range(1, wmax+1):
                if wts[i] <= w:
                    #装入与不装入 择优
                    dp[i][w] = max((dp[i-1][w-wts[i]]+vals[i]), dp[i-1][w])
                else:
                    #不可以装入
                    dp[i][w] = dp[i-1][w]
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print solution.find_max_val(6, [2, 1, 3, 5, 4], [4, 2, 3, 6, 5])
