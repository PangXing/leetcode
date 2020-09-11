# coding:utf-8

'''
【560. 和为K的子数组】
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

说明 :
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
'''

class Solution(object):
    ''' 前缀和 '''
    def subarraySum(self, nums, k):
        cnt = 0
        presums = {0: 1}
        sumpre = 0
        for i in nums:
            sumpre += i
            if (sumpre - k) in presums:
                cnt += presums[sumpre - k]
            presums.setdefault(sumpre, 0)
            presums[sumpre] += 1
        return cnt

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1]
    print solution.subarraySum(nums, 2)

