# coding:utf-8

'''
【128. 最长连续序列】
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。
示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''

class Solution(object):
    '''
    使用哈希表 优化匹配过程 降为O(1)
    '''
    def longestConsecutive(self, nums):
        if not nums:
            return  0
        nums_set = set(nums)
        start = list()
        for i in nums:
            left = i - 1
            right = i + 1
            left_flag = True if left in nums_set else False
            right_flag = True if right in nums_set else False
            if left_flag == False and right_flag == True:
                start.append(i)
        longestlist = list()
        for i in start:
            right = i + 1
            content = [i]
            while right in nums_set:
                content.append(right)
                right += 1
            if len(content) > len(longestlist):
                longestlist = content
        return len(longestlist) if longestlist else 1

if __name__ == '__main__':
    solution = Solution()
    print solution.longestConsecutive([100, 4, 200, 1, 3, 2])


