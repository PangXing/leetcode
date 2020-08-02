# coding:utf-8

class Solution(object):
    def integerBreak(self, n):
        low = n//2
        high = n -low
        interger = low * high

        if interger <= n:
            return interger
        interger_low = self.integerBreak(low)
        if interger_low < low:
            interger_low = low
        interger_high = self.integerBreak(high)
        if interger_high < high:
            interger_high = high
        return interger_low * interger_high

if __name__ == '__main__':
    solution = Solution()
    n = 10
    n = 8
    print solution.integerBreak(n)
