# coding:utf-8

'''
【42. 接雨水】
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

'''
class Solution(object):
    def trap(self, height):
        if len(height) < 3:
            return 0

        pre_list = list()
        pre_max = 0
        for i in height:
            pre_list.append(pre_max)
            if i > pre_max:
                pre_max = i
        after_list = list()
        after_max = 0
        for i in height[::-1]:
            after_list.append(after_max)
            if i > after_max:
                after_max = i
        after_list = after_list[::-1]
        res = 0
        for i in range(len(height)):
            min_high = min(pre_list[i], after_list[i])
            if min_high > height[i]:
                res += (min_high - height[i])
        return res

if __name__ == '__main__':
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print solution.trap(height)




