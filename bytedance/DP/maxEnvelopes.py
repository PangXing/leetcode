# coding:utf-8

class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        envelopes = sorted(envelopes, key=lambda x:x[0])
        dp = list()
        dp.append(1)
        for i in range(1, len(envelopes)):
            max_num = 1
            for k in range(i):
                if envelopes[k][0] < envelopes[i][0] and envelopes[k][1] < envelopes[i][1]:
                    tmp = dp[k] + 1
                    if tmp > max_num:
                        max_num = tmp
            dp.append(max_num)
        return max(dp)

if __name__ == '__main__':
    solution = Solution()
    print solution.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])

