# coding:utf-8

class Solution(object):
    def threeSum(self, nums):
        size = len(nums)
        if size < 3:
            return []
        res_set = set()
        nums.sort()
        for i in range(size):
            low = i + 1
            high = size -1
            while low < high:
                three = nums[i] + nums[low] + nums[high]
                if three == 0:
                    res_set.add((nums[i], nums[low], nums[high]))
                    low += 1
                    high -= 1
                elif three < 0:
                    low += 1
                else:
                    high -= 1
        res = list()
        for i in res_set:
            res.append(list(i))
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2,0,1,1,2]
    print solution.threeSum(nums)
