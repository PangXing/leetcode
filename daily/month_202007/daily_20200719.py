# coding:utf-8

'''
【312. 戳气球】
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。

说明:
你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

'''
from copy import deepcopy

class Solution(object):
    def __init__(self):
        self.dp = {}

    def getMaxCoins(self, nums, pts):
        key = tuple(pts)
        if key in self.dp:
            return self.dp[key]
        size = len(pts)
        max_coins = 0
        for i in range(size):
            if i == 0:
                left = 1
            else:
                left = nums[pts[i-1]]
            if i == size-1:
                right = 1
            else:
                right = nums[pts[i+1]]
            idx = pts[i]
            tmp = left * nums[idx] * right
            pts_tmp = deepcopy(pts)
            pts_tmp.pop(i)
            sumMax = self.getMaxCoins(nums, pts_tmp)
            tmp += sumMax
            if tmp > max_coins:
                max_coins = tmp
        self.dp[key] = max_coins
        return max_coins

    def maxCoins1(self, nums):
        if not nums:
            return 0
        pts = list()
        for i in range(len(nums)):
            key = tuple([i])
            self.dp[key] = nums[i]
            pts.append(i)
        return self.getMaxCoins(nums, pts)

    def maxCoins(self, nums):
        '''
        动态规则
        dp[i][j] 为开区间内 最大的coins
        '''
        if not nums:
            return 0

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in nums]

        for i in range(n-2, -1 , -1):
            for j in range(i+1, n):
                max_num = 0
                for k in range(i+1, j):
                    tmp = nums[i] * nums[k] * nums[j] #查找区间内最后一个破的位置
                    tmp += (dp[i][k] + dp[k][j])
                    if tmp > max_num:
                        max_num = tmp
                dp[i][j] = max_num
        return dp[0][n-1]



if __name__ == '__main__':
    solution = Solution()
    nums = [3,1,5,8]
    nums = [8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2]
    print solution.maxCoins(nums)
    #print solution.maxCoins1(nums)


