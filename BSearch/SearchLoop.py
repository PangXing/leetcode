# coding:utf-8

class Solution(object):
    def findloopidx(self, nums):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return left

    def search(self, nums, target):
        loopidx = self.findloopidx(nums)

        n = len(nums)
        left = 0
        right = n -1
        while left <= right:
            mid = left + (right - left)
            idx = (mid+loopidx)%n
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                left = mid + 1
            elif nums[idx] > target:
                right = mid - 1
        return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    nums = [3,1]
    print solution.search(nums, target)
