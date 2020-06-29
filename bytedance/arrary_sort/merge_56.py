# coding:utf-8

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x:x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        i = 1
        res = list()
        while i < len(intervals):
            if intervals[i][0] <= right:
                right = max(intervals[i][1], right)
            else:
                res.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
            i += 1
        res.append([left, right])
        return res

if __name__ == '__main__':
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]
    print solution.merge(intervals)