# coding:utf-8
'''
【16. 最接近的三数之和】
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''
class Solution(object):
    def threeSumClosest1(self, nums, target):
        '''
        前缀和
        '''
        size = len(nums)
        if size < 3:
            return None
        twoSunList = [ nums[0]+ nums[1]]
        closest = nums[0] + nums[1] + nums[2]
        for i in range(2, size):
            for twoSum in twoSunList:
                threeSum = twoSum + nums[i]
                if abs(threeSum - target) < abs(closest -target):
                    closest = threeSum
            for k in range(0, i):
                twoSunList.append(nums[i]+nums[k])
        return closest

    def threeSumClosest(self, nums, target):
        '''
        排序+ 双指针
        '''
        size = len(nums)
        if size < 3:
            return None
        #排序
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(size):
            low = i + 1
            high = size - 1
            while low < high:
                three = nums[i] + nums[low] + nums[high]
                if abs(three-target) < abs(closest-target):
                    closest = three
                if three < target:
                    low += 1
                elif three > target:
                    high -= 1
                else:
                    return three
        return closest


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,2,1,-4]
    target = 1
    print solution.threeSumClosest(nums, target)

