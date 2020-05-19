# coding:utf-8
import copy

'''
【题目】N皇后问题，研究如何将n个皇后放置在N*N的棋盘上，互不攻击
【分类】回溯算法
'''

class Solution(object):
    '''
    回溯算法框架：
        def backstrack(...):
            for 选择 in 选择列表：
                #做选择
                将该选择从选择列表移除
                路径.add(选择)

                backstrack(路径, 选择列表)

                #撤销选择
                路径.remove(选择)
                将该选择再次加入选择列表
    N皇后的决策树
    【路径】做成的选择，放置Q的位置
    【选择列表】可以合理选择的LIST
    【结束条件】决策树底层

    '''
    def init(self, n):
        self._size = n
        self._board = list()
        for i in range(n):
            row = list()
            for k in range(n):
                row.append('.')
            self._board.append(row)
        self._res = list()

    def fmt_res(self):
        result = list()
        for res in self._res:
            item = list()
            for k in res:
                item.append(''.join(k))
            result.append(item)
        return result

    def is_vaild(self, row, col):
        #行检测
        for col_tmp in range(self._size):
            if self._board[row][col_tmp] == 'Q':
                return False

        for row_tmp in range(self._size):
            if self._board[row_tmp][col] == 'Q':
                return False
        #左上检测
        row_tmp = row -1
        col_tmp = col - 1
        while(row_tmp >= 0 and col_tmp>=0 and row_tmp < self._size and col_tmp < self._size):
            if self._board[row_tmp][col_tmp] == 'Q':
                return False
            row_tmp -= 1
            col_tmp -= 1
        #右上检测
        row_tmp = row - 1
        col_tmp = col + 1
        while (row_tmp >= 0 and col_tmp >= 0 and row_tmp < self._size and col_tmp < self._size):
            if self._board[row_tmp][col_tmp] == 'Q':
                return False
            row_tmp -= 1
            col_tmp += 1
        # 左下检测
        row_tmp = row + 1
        col_tmp = col - 1
        while (row_tmp >= 0 and col_tmp >= 0 and row_tmp < self._size and col_tmp < self._size):
            if self._board[row_tmp][col_tmp] == 'Q':
                return False
            row_tmp += 1
            col_tmp -= 1
        # 右下检测
        row_tmp = row + 1
        col_tmp = col + 1
        while (row_tmp >= 0 and col_tmp >= 0 and row_tmp < self._size and col_tmp < self._size):
            if self._board[row_tmp][col_tmp] == 'Q':
                return False
            row_tmp += 1
            col_tmp += 1
        return True

    def solveNQueue(self, n):
        self.init(n)
        self.findNQueue(0)
        return self.fmt_res()

    def findNQueue(self, row):
        if row == self._size:
            self._res.append(copy.deepcopy(self._board))
            return

        for col in range(self._size):
            if not self.is_vaild(row, col):
                continue

            self._board[row][col] = 'Q'
            self.findNQueue(row+1)
            self._board[row][col] = '.'


if __name__ == '__main__':
    solution = Solution()
    print solution.solveNQueue(4)





