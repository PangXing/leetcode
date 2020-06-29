# coding:utf-8

'''
【300. 最长上升子序列】
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

'''


class Solution(object):
    '''
    动态规则
    '''

    def longestSubStr(self, nums):
        '''
        【dp数组定义】以i位结尾的最长子串
        【选择】max(（数字小于i位 + 1）， dp[i])
        【base】dp每一位至少为1
        '''
        if not nums:
            return 0
        dp = [1 for i in nums]
        for i in range(1, len(nums)):
            for k in range(i):
                if nums[i] > nums[k]:
                    dp[i] = max(dp[k] + 1, dp[i])
        num = max(dp)
        return num

if __name__ == '__main__':
    solution = Solution()
    print solution.longestSubStr([10, 9, 2, 5, 3, 7, 101, 18])
    print solution.longestSubStr([10, 9, 2, 5, 3, 7, 9, 1, 8, 12])

