# coding:utf-8

'''
【974.和可被K整除的子数组】
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

'''

class Solution(object):
    '''
    前缀和 + 状态压缩
    '''
    def subarrayDivByK(self, A, K):
        div_dict = {0: 1} #初始化-无数据的情况 容易遗漏
        pre_sum = 0
        res = 0
        for i in A:
            pre_sum += i
            div_num = pre_sum%K
            if div_num in div_dict:
                res += div_dict[div_num]
            div_dict.setdefault(div_num, 0)
            div_dict[div_num] += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.subarrayDivByK([4, 5, 0, -2, -3, 1], 5)