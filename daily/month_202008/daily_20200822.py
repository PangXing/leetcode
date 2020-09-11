# coding:utf-8

class Solution(object):
    def copylist(self, nums, i, k):
        res = list()
        for j in range(len(nums)):
            if j == i or j == k:
                continue
            res.append(nums[j])
        return res

    def judgePoint24(self, nums):
        n = len(nums)
        if n == 1:
            diff = nums[0] - 24
            flag = True if abs(diff) < 0.001 else False
            return flag

        for i in range(n):
            for k in range(n):
                if i == k:
                    continue
                tmp_list = self.copylist(nums, i, k)

                tmp = nums[i] + nums[k]
                tmp_list.append(tmp)
                if self.judgePoint24(tmp_list):
                    return True

                tmp_list.pop()
                tmp = nums[i] - nums[k] if  nums[i] > nums[k] else nums[k] - nums[i]
                tmp_list.append(tmp)
                if self.judgePoint24(tmp_list):
                    return True

                tmp_list.pop()
                tmp = nums[i] * nums[k]
                tmp_list.append(tmp)
                if self.judgePoint24(tmp_list):
                    return True

                if nums[k] != 0:
                    tmp_list.pop()
                    tmp = float(nums[i]) / nums[k]
                    tmp_list.append(tmp)
                    if self.judgePoint24(tmp_list):
                        return True

                if nums[i] != 0:
                    tmp_list.pop()
                    tmp = float(nums[k]) / nums[i]
                    tmp_list.append(tmp)
                    if self.judgePoint24(tmp_list):
                        return True
        return False

if __name__ == '__main__':
    solution = Solution()
    nums = [4, 1, 8, 7]
    nums = [8,1,6,6]
    nums = [1,5,9,1]
    nums = [3,3,8,8]
    #nums = [8,1,6,6]

    print solution.judgePoint24(nums)


