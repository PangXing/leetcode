# coding:utf-8
'''
【9. 回文数】
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:
你能不将整数转为字符串来解决这个问题吗？
'''

class Solution(object):
    def isPalindrome2(self, x):
        x_str = str(x)
        low = 0
        high = len(x_str) -1
        while low < high:
            if x_str[low] != x_str[high]:
                return False
            low += 1
            high -= 1
        return True

    def isPalindrome(self, x):
        if (x < 0) or (x > 0 and x%10 == 0):
            return False
        num = 0
        s = 1
        while s <= x:
            s = s*10
            num = num*10 + x%10
            x = x / 10

        return (x == num) | (x == num/10)

if __name__ == '__main__':
    solution = Solution()
    print solution.isPalindrome(21120)