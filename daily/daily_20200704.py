# coding:utf-8

'''
【32. 最长有效括号】
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''

class Solution(object):
    def longestValidParentheses(self, s):
        if not s:
            return 0
        flags = [False for i in s]
        stack = list()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    left = stack.pop()
                    flags[left] = True
                    flags[i] = True
        low = 0
        high = 0
        max_len = 0
        while high < len(flags):
            if flags[high]:
                tmp = high + 1 - low
                if tmp > max_len:
                    max_len = tmp
            else:
                low = high + 1
            high += 1
        return max_len

if __name__ == '__main__':
    solution = Solution()
    s = ")()())"
    print solution.longestValidParentheses(s)







