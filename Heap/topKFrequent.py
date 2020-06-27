# coding:utf-8

'''
【347. 前 K 个高频元素】
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]
 

提示：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
'''

from Queue import PriorityQueue

class Solution(object):
    '''
    Hash 统计 + 优先队列
    '''
    def topKFrequent(self, nums, k):
        frequent = dict()
        for i in nums:
            frequent.setdefault(i, 0)
            frequent[i] += 1
        q = PriorityQueue()
        for num, cnt in frequent.items():
            if q.qsize() == k:
                val, key = q.get()
                if cnt > val:
                    q.put((cnt, num))
                else:
                    q.put((val, key))
            else:
                q.put((cnt, num))
        res = list()
        for i in q.queue:
            res.append(i[1])
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print solution.topKFrequent(nums, k)