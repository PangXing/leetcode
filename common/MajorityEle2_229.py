# coding:utf-8

'''
【229. 求众数 II】
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:
输入: [3,2,3]
输出: [3]

示例 2:
输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
'''
class Solution(object):
    '''
    摩尔投票法
    组一个team 若投票到team中的一员 进行下一轮，否则同时抵消；最终team中为最大的几个人
    '''
    def majoritElement(self, nums):
        nums_set = set(nums)
        if len(nums) < 3 or len(nums_set) < 2:
            return list(nums_set)

        #投票过程
        cond1 = nums_set.pop()
        count1 = 0
        cond2 = nums_set.pop()
        count2 = 0
        for i in nums:
            if i == cond1:
                count1 += 1
            elif i == cond2:
                count2 += 1
            else:
                if count1 <= 0:
                    cond1 = i
                    count1 = 1
                if count2 <= 0:
                    cond2 = i
                    count2 = 1
                else:
                    count1 -= 1
                    count2 -= 1

        #审核过程
        cnt1 = 0
        cnt2 = 0
        for i in nums:
            if i == cond1:
                cnt1 += 1
            if i == cond2:
                cnt2 += 1
        res = set()
        if cnt1 * 3 > len(nums):
            res.add(cond1)
        if cnt2 * 3 > len(nums):
            res.add(cond2)
        return list(res)

if __name__ == '__main__':
    solution = Solution()
    print solution.majoritElement([1,1,1,2,3,4,5,6])