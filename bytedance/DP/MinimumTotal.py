# coding:utf-8

class Solution(object):
    def minimumTotal(self, triangle):
        dp = [[triangle[0][0]]]
        for row in range(1, len(triangle)):
            dp.append(list())
            dp[row].append(dp[row - 1][0] + triangle[row][0])
            for col in range(1, len(triangle[row]) - 1):
                total = min(dp[row - 1][col - 1] + triangle[row][col],
                            dp[row - 1][col] + triangle[row][col])
                dp[row].append(total)
            dp[row].append(dp[row-1][len(triangle[row])-2] + triangle[row][-1])
        return min(dp[-1])


if __name__ == '__main__':
    solution = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print solution.minimumTotal(triangle)
