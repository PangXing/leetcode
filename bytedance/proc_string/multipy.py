# coding:utf-8

class Solution(object):
    def multiply(self, num1, num2):
        res = 0
        for i in num1:
            res1 = 0
            for k in num2:
                res1 = res1 * 10 + int(i) * int(k)
            res = res * 10 + res1
        return str(res)

if __name__ == '__main__':
    solution = Solution()
    print solution.multiply('123', '456')
    print solution.multiply('2', '3')