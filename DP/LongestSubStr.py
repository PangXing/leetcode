# coding:utf-8

'''
【题目】最长递增无序整数数组，找到其中最长的上升子序列长度
【类别】动态规划
'''


class Solution(object):

    def longestSubStr(self, l1):
        '''
        【dp数组定义】以i位结尾的最长子串
        【选择】max(（数字小于i位 + 1）， dp[i])
        【base】dp每一位至少为1
        '''
        dp = [1 for i in l1]
        for i in range(1, len(l1)):
            for k in range(i):
                if l1[i] > l1[k]:
                    dp[i] = max(dp[k] + 1, dp[i])
        num = max(dp)
        return num

if __name__ == '__main__':
    solution = Solution()
    print solution.longestSubStr([10, 9, 2, 5, 3, 7, 101, 18])
    print solution.longestSubStr([10, 9, 2, 5, 3, 7, 9, 1, 8, 12])

