# coding:utf-8

'''
【287】寻找重复数
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
'''

class Solution(object):
    def findDuplicate(self, nums):
        '''
        二分查找
        cnt[i] 小于等于i的个数

        要求log(n)的时间复杂度 n(1)空间复杂度 想到二分查找
        '''
        size = len(nums)
        low = 1
        high = size - 1
        index = -1
        while low <= high:
            mid = low + (high - low) / 2
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid - 1
                index = mid
        return index


if __name__ == '__main__':
    solution = Solution()
    print solution.findDuplicate([1, 3, 4, 2, 2])
