# coding:utf-8

class Solution(object):
    def threeSum(self, nums):
        if not nums:
            return []
        nums.sort()
        res = list()
        low = 0
        high = len(nums) -1
        while low < high:
            mid = 0 - (nums[low]+nums[high])
            if mid > nums[high]:
                high -= 1
                while nums[high] == nums[high+1] and low < high:
                    high -= 1
            else:
                if mid in nums[low+1: high]:
                    res.append([nums[low], mid, nums[high]])

                low += 1
                while nums[low] == nums[low-1] and low < high:
                    low += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    #nums = [-2,0,1,1,2]
    print solution.threeSum(nums)
