# coding:utf-8

class Solution(object):
    def searchLeft(self, nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] == target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def searchRight(self, nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        if right < 0 or nums[right] != target:
            return -1
        return right

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        left = self.searchLeft(nums, target)
        if left == -1:
            return [-1, -1]

        right = self.searchRight(nums, target)
        return [left, right]

if __name__ == '__main__':
    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 6
    print solution.searchRange(nums, target)


