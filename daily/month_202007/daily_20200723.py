# coding:utf-8
class Solution(object):
    def minPathSum(self, grid):
        dp = list()
        for i in range(len(grid)):
            dp.append(list())
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    dp[i].append(grid[i][j])
                elif i == 0:
                    dp[i].append(dp[i][j-1] + grid[i][j])
                elif j == 0:
                    dp[i].append(dp[i-1][j] + grid[i][j])
                else:
                    dp[i].append(min(dp[i-1][j], dp[i][j-1]) + grid[i][j])
        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    grid = [ [1,3,1],
             [1,5,1],
             [4,2,1]
             ]
    print solution.minPathSum(grid)



