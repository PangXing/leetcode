# coding:utf-8

class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums or sum(nums) < s:
            return 0
        low = 0
        high = 0
        min_num = len(nums) + 1
        while high < len(nums):
            while low <= high and sum(nums[low:high+1]) >= s:
                tmp = high + 1 - low
                if tmp < min_num:
                    min_num = tmp
                if min_num == 1:
                    return 1
                low += 1
            high += 1
        return min_num

if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,2,4,3]
    print solution.minSubArrayLen(7, nums)

