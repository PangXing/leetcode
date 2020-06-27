# coding:utf-8

'''
【78. 子集】
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
import copy

class Solution(object):
    def subsets(self, nums):
        if not nums:
            return [[]]
        res = list()
        num = nums[0]
        sub_res = self.subsets(nums[1:])
        for i in sub_res:
            res.append(i)
            tmp = copy.deepcopy(i)
            tmp.append(num)
            res.append(tmp)
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.subsets([1,2,3])
