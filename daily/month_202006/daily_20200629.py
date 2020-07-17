# coding:utf-8

from Queue import PriorityQueue

class Solution(object):
    def findKthLargest(self, nums, k):
        if len(nums) < k:
            return None
        q = PriorityQueue()
        for i in nums:
            if q.qsize() == k:
                top = q.get()
                if i > top:
                    q.put(i)
                else:
                    q.put(top)
            else:
                q.put(i)
        return q.get()

if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    print solution.findKthLargest(nums, 4)

