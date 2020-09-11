# coding:utf-8

class Solution(object):
    def MaxSum(self, nums, isFirst):
        if not nums:
            return (0, 0)
        if isFirst:
            sum_a_1, sum_b_1 = self.MaxSum(nums[1:], False)
            sum_a_2, sum_b_2 = self.MaxSum(nums[:-1], False)
            tmp1 = sum_a_1 + nums[0]
            tmp2 = sum_a_2 + nums[-1]
            if tmp1 > tmp2:
                sum_a = tmp1
                sum_b = sum_b_1
            else:
                sum_a = tmp2
                sum_b = sum_b_2
        else:
            sum_a_1, sum_b_1 = self.MaxSum(nums[1:], True)
            sum_a_2, sum_b_2 = self.MaxSum(nums[:-1], True)
            tmp1 = sum_b_1 + nums[0]
            tmp2 = sum_b_2 + nums[-1]
            if tmp1 > tmp2:
                sum_b = tmp1
                sum_a = sum_a_1
            else:
                sum_b = tmp2
                sum_a = sum_a_2
        return sum_a, sum_b


    def PredictTheWinner(self, nums):
        sum_a, sum_b = self.MaxSum(nums, True)
        return sum_a >= sum_b

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 5, 2]
    print solution.PredictTheWinner(nums)
