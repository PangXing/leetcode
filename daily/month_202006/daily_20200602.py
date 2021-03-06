# coding:utf-8

'''
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
输入: n = 3
输出: 6

示例 2：
输入: n = 9
输出: 45

限制：
1 <= n <= 10000
'''

class Solution(object):
    '''
    递归 + 逻辑短路
    '''
    def __init__(self):
        self._res = 0

    def sumNums(self, n):
        n > 1 and self.sumNums(n-1)
        self._res += n
        return self._res

if __name__ == '__main__':
    solution = Solution()
    print solution.sumNums(9)