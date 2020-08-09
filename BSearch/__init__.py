# coding:utf-8

'''
https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/

- 不要出现else，而是把所有情况用elif 写清楚，这样可以清楚展示所有细节
- 搜索区间为 [left, right] 闭区间
- left = mid+1 right = mid -1
'''

# 查找一个数
def binarySearch(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right:              #细节一
        mid = left + (right-left)/2
        if nums[mid] == target:
            return mid                #细节二
        elif nums[mid] < target:
            left = mid + 1            #细节三
        elif nums[mid] > target:
            right = mid -1            #细节四
    return -1                         #细节五

#查找左边界
def binarySearch_left(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right:              #细节一
        mid = left + (right-left)/2
        if nums[mid] == target:
            right = mid -1            #细节二
        elif nums[mid] < target:
            left = mid + 1            #细节三
        elif nums[mid] > target:
            right = mid -1            #细节四
    if left >= len(nums) or nums[left] != target:
        return -1
    return left                         #细节五

#查找右边界
def binarySearch_right(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right:              #细节一
        mid = left + (right-left)/2
        if nums[mid] == target:
            left = mid + 1            #细节二
        elif nums[mid] < target:
            left = mid + 1            #细节三
        elif nums[mid] > target:
            right = mid -1            #细节四
    if right < 0 or nums[right] != target:
        return -1
    return right                         #细节五

