# coding:utf-8

'''
【91. 解码方法】
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:
输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2:
输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
'''

class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        if n < 1:
            return 0
        if int(s[0]) == 0:
            return 0
        if n == 1 :
            return 1
        dp = list()
        dp.append(1)
        dp.append(1)
        for i in range(2, n+1):
            tmp = int(s[i-2:i])
            if tmp == 10 or tmp == 20:
                dp.append(dp[i - 2])
            elif 10 < tmp < 27:
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i-1]) != 0:
                dp.append(dp[i - 1])
            else:
                return 0
        return dp[n]

if __name__ == '__main__':
    solution = Solution()
    s = '101'
    print solution.numDecodings(s)

