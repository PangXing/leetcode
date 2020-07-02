# coding:utf-8

'''
【378. 有序矩阵中第K小的元素】
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。
 
提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
'''

from Queue import PriorityQueue

class Solution(object):
    def kthSmallest1(self, matrix, k):
        '''
        优先队列
        '''
        q = PriorityQueue()
        n = len(matrix)
        limit = n*n - k + 1
        for i in matrix:
            for k in i:
                if q.qsize() == limit:
                    tmp = q.get()
                    if tmp < k:
                        q.put(k)
                    else:
                        q.put(tmp)
                else:
                    q.put(k)
        return q.get()

    def kthSmallest(self, matrix, k):
        '''
        二分查找
        '''
        def _check(mid):
            row = len(matrix) - 1
            col = 0
            num = 0
            while row >= 0 and col < len(matrix):
                if mid >= matrix[row][col]:
                    num += (row + 1)
                    col += 1
                else:
                    row -= 1
            return num >= k

        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = left + (right-left)/2
            if _check(mid):
                right = mid
            else:
                left = mid +1
        return left


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    print solution.kthSmallest(matrix, 8)

