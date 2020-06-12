# coding:utf-8

class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        preSum = dict()
        for i in range(len(nums)-1):
            for k in range(i+1, len(nums)):
                sum2 = nums[i] + nums[k]
                preSum.setdefault(sum2, [])
                preSum[sum2].append([i, k])
        res = list()
        for i in range(len(nums)):
            d_sum = 0 - nums[i]
            pre_list = preSum.get(d_sum, [])
            for k in pre_list:
                low = k[0]
                high = k[1]
                if i != low and i != high and i < low < high:
                    res.append([nums[i], nums[low], nums[high]])

        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.threeSum([-1, 0, 1, 2, -1, -4])
