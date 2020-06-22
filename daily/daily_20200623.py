# coding:utf-8

'''
【67. 二进制求和】
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
 

提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
'''

class Solution(object):
    def addByBinary(self, l, r, pre):
        sum_d = int(l) + int(r) + int(pre)
        if sum_d == 0:
            return '0', '0'
        elif sum_d == 1:
            return '0', '1'
        elif sum_d == 2:
            return '1', '0'
        else:
            return '1', '1'

    def addBinary(self, a, b):
        if not a:
            return b
        if not b:
            return a
        res = ''
        pos_a = len(a) -1
        pos_b = len(b) -1
        pre = '0'
        while pos_a >= 0 or pos_b >= 0:
            a_str = '0' if pos_a < 0 else a[pos_a]
            b_str = '0' if pos_b < 0 else b[pos_b]
            pre, tmp = self.addByBinary(a_str, b_str, pre)
            res = tmp + res
            pos_a -= 1
            pos_b -= 1
        if pre == '0':
            return res
        else:
            return pre+res

if __name__ == '__main__':
    solution = Solution()
    a = "1010"
    b = "1011"
    print solution.addBinary(a, b)


