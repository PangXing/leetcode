# coding:utf-8

class Solution(object):
    def isSubsequence(self, s, t):
        p = -1
        n = len(t)
        for i in s:
            p += 1
            while p < n and i != t[p]:
                p += 1
            if p == n:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    s = 'abc'
    t = 'ahbgdc'
    # s = 'axc'
    # s = 'aaaaaa'
    # t = 'bbaaaa'
    print solution.isSubsequence(s, t)

