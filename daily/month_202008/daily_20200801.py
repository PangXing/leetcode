# coding:utf-8

class Solution(object):
    def findMix(self, l1, start, num):
        idx = start
        if l1[start] < num :
            tmp = start + 1
            while tmp < len(l1) and l1[tmp] < num:
                tmp += 1
            if tmp == len(l1):
                idx == tmp -1
            else:
                idx = tmp if abs(l1[tmp]- num) < abs(l1[tmp-1] -num) else tmp - 1
        return idx

    def smallestRange(self, nums):
        if len(nums) == 1:
            return [nums[0], nums[0]]

        small_idx = 0
        for i in range(1, len(nums)):
            if len(nums[small_idx]) > len(nums[i]):
                small_idx = i
        small_one = nums.pop(small_idx)

        smallest_range = [-float('inf'), float('inf')]
        smallest_len = float('inf')
        dp = [0]*len(nums)
        for i in small_one:
            tmp_list = [i]
            for k in range(len(nums)):
                idx = self.findMix(nums[k], dp[k], i)
                dp[k] = idx
                tmp_list.append(nums[k][idx])
            tmp_list.sort()
            tmp_len = tmp_list[-1] - tmp_list[0]
            if tmp_len < smallest_len:
                smallest_len = tmp_len
                smallest_range = [tmp_list[0], tmp_list[-1]]
        return smallest_range

if __name__ == '__main__':
    solution = Solution()
    nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    print solution.smallestRange(nums)


