# coding:utf-8

'''
【97. 交错字符串】
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true

示例 2:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
'''

class Solution(object):
    def __init__(self):
        self.dp = dict()

    def isInterleave(self, s1, s2, s3):
        '''
        dfs + 记忆剪枝
        '''
        key = '%s_%s_%s' %(s1, s2, s3)
        if key in self.dp:
            return self.dp[key]

        flag = False
        if not s1:
            flag = (s2 == s3)
        elif not s2:
            flag = (s1 == s3)
        elif not s3:
            flag = (s1 and s2)
        else:
            if s1[0] == s3[0]:
                flag = self.isInterleave(s1[1:], s2, s3[1:])
            if not flag and s2[0] == s3[0]:
                flag = self.isInterleave(s1, s2[1:], s3[1:])
        self.dp[key] = flag
        return flag

if __name__ == '__main__':
    solution = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbbaccc"
    # s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    # s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    # s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    print solution.isInterleave(s1, s2, s3)