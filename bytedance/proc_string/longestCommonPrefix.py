# coding:utf-8

class Solution(object):
    def longestCommonPrefix(self, strs):
         if not strs:
             return ''
         if len(strs) == 1 or len(strs[0]) == 0:
             return strs[0]
         begin = strs[0]
         size = len(begin)
         for i in range(size):
             k = begin[i]
             for s in strs:
                 if len(s) <= i:
                     return s
                 if s[i] != k:
                     return s[:i]
         return begin

if __name__ ==  '__main__':
    solution = Solution()
    print solution.longestCommonPrefix(["flower","flow","flight"])
    print solution.longestCommonPrefix(["dog","racecar","car"])