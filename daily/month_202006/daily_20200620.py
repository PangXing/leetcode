# coding:utf-8
'''
【10. 正则表达式匹配】
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
'''

class Solution(object):
    def isMatch_1(self, s, p):
        '''
        暴力枚举
        '''
        if s == '' and p == '':
            return True
        if p == '':
            return False
        if s == '':
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False
        is_match = True if p[0] in [s[0], '.'] else False
        if len(p) > 1 and p[1] == '*':
            res1 = False
            if is_match:
                res1 =  self.isMatch(s[1:], p)
            res2 = self.isMatch(s, p[2:])
            return res1 or res2
        else:
            if is_match:
                return self.isMatch(s[1:], p[1:])
            else:
                return False

    def isMatch(self, s, p):
        '''
        动态规则
        '''
        demo = dict()
        def dp(i, j):
            if (i, j) in demo: return demo[(i, j)]
            if i == len(s) and j==len(p):
                return True
            if j == len(p):
                return False
            if i == len(s):
                if j + 1 < len(p) and p[j+1] == '*':
                    return dp(i, j+2)
                else:
                    return False
            is_match = True if p[j] in [s[i], '.'] else False
            if j + 1 < len(p) and p[j+1] == '*':
                res = dp(i, j+2) or (is_match and dp(i+1, j))
            else:
                res = is_match and dp(i+1, j+1)
            demo[(i, j)] = res
            return res

        return dp(0, 0)


if __name__ == '__main__':
    solution = Solution()
    print solution.isMatch("aa", "a")
    print solution.isMatch("aa", "a*")
    print solution.isMatch("aab", "c*a*b")
    print solution.isMatch("mississippi", "mis*is*p*.")
    print solution.isMatch("a", ".*..a*")

