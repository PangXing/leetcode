# coding:utf-8

'''
【415. 字符串相加】
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''

class Solution(object):

    def addStrings(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)
        nxt = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        pos = 0
        rep = ''
        while pos < n1 or pos < n2:
            if pos < n1 and pos < n2:
                res = int(num1[pos]) + int(num2[pos]) + nxt
            elif pos < n1:
                res = int(num1[pos]) + nxt
            else:
                res = int(num2[pos]) + nxt
            if res > 9:
                nxt = 1
                rep += str(res-10)
            else:
                nxt = 0
                rep += str(res)
            pos += 1

        if nxt:
            rep += '1'
        return rep[::-1]

if __name__ == '__main__':
    solution = Solution()
    num1 = '999'
    num2 = '9999'
    print solution.addStrings(num1, num2)






