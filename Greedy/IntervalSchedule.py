# coding:utf-8

class Solution(object):
    def interval_schedule(self, intvs):
        #按照结束时间，升序排序
        intvs_sorted = sorted(intvs, key= lambda x: x[1])
        x = intvs_sorted[0]
        res = [x]
        for i in intvs_sorted[1:]:
            if x[1] > i[0]:
                continue
            res.append(i)
            x = i
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.interval_schedule([[1,3], [2,4], [3,6]])