# coding:utf-8

'''
[4, 3 ,2 ,1 ,1, 1, 2,3, 4, 5]

output 1
logN
[3 ,3, 3, 3, 3,1,2]

[4, 3, 2, 1, 3, 5, 6, 7, 8]
'''

class Solution(object):


    def findMin(self, l1):
        if len(l1) < 3:
            return min(l1[0], l1[1])
        low = 0
        high = len(l1)
        while low <= high:
            mid = low + (high - low)/2
            item = l1[mid]
            pre = l1[mid-1]
            after = l1[mid+1]

            while item == l1[pre] and pre >= low:
                pre -= 1
            while item == l1[after] and after <= high:
                after += 1

            if item <= l1[pre] and item <= l1[after]:
                return [pre, after]

            elif item > l1[pre]:
                high = mid
            elif item > l1[after]:
                low = mid





