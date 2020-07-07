# coding:utf-8

'''
【面试题 16.11. 跳水板】
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
返回的长度需要从小到大排列。

示例：
输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}

提示：
0 < shorter <= longer
0 <= k <= 100000
'''

class Solution(object):
    def divingBoard(self, shorter, longer, k):
        if k == 0:
            return []
        if shorter == longer:
            return [shorter*k]
        res = list()
        res_set = set()
        for i in range(k+1):
            s_len = k - i
            l_len = i
            num = shorter * s_len + longer * l_len
            if num not in res_set:
                res.append(num)
                res_set.add(num)
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.divingBoard(1, 2, 3)