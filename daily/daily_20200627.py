# coding:utf-8

'''
【41. 缺失的第一个正数】
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1
 
提示：
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
'''

class Solution(object):
    def firstMissingPositive1(self, nums):
        '''
        使用了hash表 ，空间复杂度大于 O(1)
        '''
        positive_set = set()
        for i in nums:
            if i > 0:
                positive_set.add(i)
        for i in xrange(1, len(nums)+1):
            if i not in positive_set:
                return i
        return len(nums)+1

    def firstMissingPositive(self, nums):
        if 1 not in nums:
            return 1
        n = len(nums)
        #不关心非整数 与 大于n的整数
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 1
        #使用数组的下标作为hash
        for i in nums:
            idx = abs(i)
            nums[idx-1] = - abs(nums[idx-1])
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1



if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,0]
    #nums = [7,8,9,11,12]
    nums = [3,4,-1,1]
    print solution.firstMissingPositive(nums)