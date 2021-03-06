# coding:utf-8

'''
【面试题46. 把数字翻译成字符串】
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 
提示：
0 <= num < 2[31]

'''
class Solution(object):
    '''
    动态规划
    '''
    def translateNum(self, num):
        num_list = list()
        for i in str(num):
            num_list.append(int(i))
        if len(num_list) == 1:
            return 1

        dp = [0 for i in num_list]
        dp[-1] = 1
        k = num_list[-2] * 10 + num_list[-1]
        if 10 <= k < 26:
            dp[-2] = 2
        else:
            dp[-2] = 1
        if len(num_list) > 2:
            for i in range(len(num_list)-3, -1, -1):
                dp[i] = dp[i+1]
                k = num_list[i] * 10 + num_list[i+1]
                if 10 <= k < 26:
                    dp[i] += dp[i+2]
        return dp[0]

if __name__ == '__main__':
    solution = Solution()
    print solution.translateNum(12258)

