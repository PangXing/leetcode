# coding:utf-8

class Solution(object):
    def __init__(self):
        self._res = 0

    def findTargetSumWays(self, nums, S):
        if not nums and S == 0:
            self._res += 1

