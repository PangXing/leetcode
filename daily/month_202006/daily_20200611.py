# coding:utf-8

'''
【739 每日温度】
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
'''
class Solution(object):
    '''
    单调栈
    '''
    def dailyTemperatures(self, T):
        res = list()
        min_stact = list()
        for i in range(len(T)-1, -1, -1):
            while min_stact and T[min_stact[-1]] <= T[i]:
                min_stact.pop()
            latest = min_stact[-1]-i if min_stact else 0
            res.append(latest)
            min_stact.append(i)
        res.reverse()
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print solution.dailyTemperatures([89,62,70,58,47,47,46,76,100,70])

