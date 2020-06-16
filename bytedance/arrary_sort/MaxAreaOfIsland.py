# coding:utf-8

'''
【695. 岛屿的最大面积】
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)


示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。
'''

class UnionFind(object):
    def __init__(self, n):
        self._parents = list()
        self._sizes = list()
        self._num = n

        for i in range(n):
            self._parents.append(i)
            self._sizes.append(1)

    def find(self, p):
        while self._parents[p] != p:
            self._parents[p] = self._parents[self._parents[p]]
            p = self._parents[p]
        return self._parents[p]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p != root_q:
            if self._sizes[root_p] > self._sizes[root_q]:
                self._parents[root_q] = root_p
                self._sizes[root_p] += self._sizes[root_q]
            else:
                self._parents[root_p] = root_q
                self._sizes[root_q] += self._sizes[root_p]

    def find_max_size(self):
        return max(self._sizes)


class Solution(object):
    def maxAreaOfIsland(self, grid):
        row_len = len(grid)
        col_len = len(grid[0])
        uf = UnionFind(row_len * col_len)
        has_island = False
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1:
                    has_island = True
                    idx = row * col_len + col
                    # 向右搜索
                    right_col = col + 1
                    if right_col < col_len and grid[row][right_col] == 1:
                        idx2 = row * col_len + right_col
                        uf.union(idx, idx2)
                    # 向下搜索
                    down_row = row + 1
                    if down_row < row_len and grid[down_row][col] == 1:
                        idx2 = down_row * col_len + col
                        uf.union(idx, idx2)
        if has_island:
            return uf.find_max_size()
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print solution.maxAreaOfIsland(grid)