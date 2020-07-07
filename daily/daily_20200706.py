# coding:utf-8

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[n-1][m-1]:
            return 0
        dp = list()
        for row in range(n):
            dp.append(list())
            for col in range(m):
                if row == 0 and col == 0:
                    dp[row].append(1)
                elif obstacleGrid[row][col]:
                    dp[row].append(0)
                elif row == 0:
                    dp[row].append(dp[row][col-1])
                elif col == 0:
                    dp[row].append(dp[row-1][col])
                else:
                    dp[row].append(dp[row-1][col] + dp[row][col-1])
        return dp[n-1][m-1]

if __name__ == '__main__':
    solution = Solution()
    grid = [[0,0,0],
            [0,1,0],
            [0,0,0]]
    print solution.uniquePathsWithObstacles(grid)

