# coding:utf-8

'''
【215. 数组中的第K个最大元素】
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
'''

from Queue import PriorityQueue

class Solution(object):
    def findKthLargest(self, nums, k):
        if len(nums) < k or k <= 0:
            return None
        q = PriorityQueue()
        for i in nums:
            if q.qsize() == k:
                v = q.get()
                if v < i:
                    q.put(i)
                else:
                    q.put(v)
            else:
                q.put(i)
        return q.get()

if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print solution.findKthLargest(nums, k)

