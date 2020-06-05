# coding:utf-8
'''
【238. 除自身以外数组的乘积】
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
示例:
输入: [1,2,3,4]
输出: [24,12,8,6]

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''

class Solution(object):
    '''
    乘积 = 前缀元素乘积 * 后缀元素乘积
    '''
    def productExceptSelf_1(self, nums):
        size = len(nums)
        preExcept = list()
        preExcept.append(1)
        for i in range(1, size):
            pre = nums[i-1] * preExcept[-1]
            preExcept.append(pre)
        afterExcept = list()
        afterExcept.append(1)
        for i in range(size-2, -1, -1):
            after = nums[i+1] * afterExcept[-1]
            afterExcept.append(after)
        output = list()
        for i in range(size):
            res = preExcept[i] * afterExcept[size-1-i]
            output.append(res)
        return output

    def productExceptSelf(self, nums):
        size = len(nums)
        output = list()
        output.append(1)
        for i in range(1, size):
            pre = nums[i - 1] * output[-1]
            output.append(pre)
        R = 1
        for i in range(size - 2, -1, -1):
            R = nums[i + 1] * R
            output[i] = output[i] * R
        return output

if __name__ == '__main__':
    solution = Solution()
    print solution.productExceptSelf([1,2,3,4])