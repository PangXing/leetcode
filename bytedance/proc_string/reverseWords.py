# coding:utf-8

class Solution(object):
    def reverse(self, s):
        s = s.strip()
        s = list(s)
        low = 0
        high = len(s) -1
        while low < high:
            tmp = s[low]
            s[low] = s[high]
            s[high] = tmp
            low += 1
            high -= 1
        return ''.join(s)

    def reverseWords(self, s):
        s = self.reverse(s)
        res = ''
        low = 0
        high = 0
        while high < len(s):
            if s[high] == ' ':
                tmp = self.reverse(s[low:high+1])
                if tmp:
                    res = res + tmp + ' '
                low = high+1
            high += 1
        res += self.reverse(s[low:high+1])
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.reverseWords('the sky is blue')
    print solution.reverseWords('  hello world!  ')
    print solution.reverseWords('a good   example')


