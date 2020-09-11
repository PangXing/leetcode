# coding:utf-8

#  l1 = [1, ..., 100000]
# s

# l1 = [-1, 1, 2, 3, 4, 5] s= 6

def search(l2, num):
    #二分查找
    low = 0
    high = len(l2)
    while low <= high:
        mid = low + (high-low)/2
        if l2[mid] == num:
            return mid
        elif l2[mid] > num:
            high = mid - 1
        elif l2[mid] < num:
            low = mid + 1
    return -1

def findSum(l1 , s):
    low = 0
    high = len(l1)
    while low < high:
        if sum1 == s:
            return True
        elif sum2 == s:
            return True
        elif sum1 > s:
            high = mid -1
        elif sum2 < s:
            low += 1
    return False
