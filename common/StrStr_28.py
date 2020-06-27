# coding:utf-8

'''
【28. 实现 strStr()】
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
'''
class Solution(object):
    def strStr1(self, haystack, needle):
        if not needle:
            return 0
        low = 0
        high = 0
        size = len(needle)
        while high < len(haystack):
            if haystack[high] in needle:
                if (high+1) - low == size:
                    if haystack[low:high+1] == needle:
                        return low
                    else:
                        low += 1
            else:
                low = high+1
            high += 1
        return -1

    def strStr(self, haystack, needle):
        if not needle:
            return 0
        L = len(needle)
        for i in range(len(haystack)- L + 1):
            if haystack[i: i+L] == needle:
                return i
        return -1

if __name__ == '__main__':
    solution = Solution()
    haystack = 'hello'
    needle = 'll'
    print solution.strStr(haystack, needle)


