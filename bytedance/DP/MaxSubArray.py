# coding:utf-8

'''
【53. 最大子序和】
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''

class Solution(object):
    def maxSubArray(self, nums):
        dp = list()
        dp.append(nums[0])
        maxSum = dp[0]
        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp.append(nums[i])
            else:
                dp.append(dp[i-1] + nums[i])
            if dp[i] > maxSum:
                maxSum = dp[i]
        return maxSum

if __name__ == '__main__':
    solution = Solution()
    print solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
