# coding:utf-8

class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        left = 0
        right = 1
        size = len(nums)
        max_len = 1
        while right < size:
            if nums[right] > nums[right-1]:
                tmp = right - left + 1
                if tmp > max_len:
                    max_len = tmp
            else:
                left = right
            right += 1
        return max_len

if __name__ == '__main__':
    solution = Solution()
    print solution.findLengthOfLCIS([1,3,5,4,7])
