# coding:utf-8

'''
【44. 通配符匹配】
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。

示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

示例 4:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

示例 5:
输入:
s = "acdcb"
p = "a*c?b"
输出: false
'''

class Solution(object):
    def _find_next(self, s, start_list, p):
        res = set()
        n = len(s)
        for i in start_list:
            if i < 0:
                if p == '*':
                    res.add(i)
                else:
                    nxt = abs(i)
                    while nxt <= n:
                        if p == '?' or s[nxt-1] == p:
                            res.add(nxt)
                        nxt += 1
            else:
                nxt = i + 1
                if p == '*':
                    res.add(-nxt)
                if nxt <= n:
                    if p == '?' or s[nxt-1] == p:
                        res.add(nxt)
        return list(res)

    def isMatch(self, s, p):
        n = len(s)
        n_p = len(p)
        if n == 0 and n_p == 0:
            return True
        elif n > 0 and n_p == 0:
            return False
        dp = list()
        dp.append([0])
        for i in range(n_p):
            start_list = dp[i]
            nxt_list = self._find_next(s, start_list, p[i])
            if not nxt_list:
                return False
            else:
                dp.append(nxt_list)

        if dp[n_p]:
            for i in dp[n_p]:
                if i < 0 or i == n:
                    return True
        return False

if __name__ == '__main__':
    solution = Solution()
    s = 'adceb'
    p = '*a*b'
    s = 'aa'
    p = '*'
    s = "adceb"
    p = '*a*b'
    s = ''
    p = '*'
    s = 'b'
    p = '?*?'
    print solution.isMatch(s, p)



