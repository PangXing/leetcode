# coding:utf-8

class Solution(object):
    def check(self, board, click):
        row = click[0]
        col = click[1]
        rows = len(board)
        cols = len(board[0])
        cnt = 0
        if row - 1 >= 0 and board[row - 1][col] == 'M':
            cnt += 1
        if row + 1 < rows and board[row + 1][col] == 'M':
            cnt += 1
        if col - 1 >= 0 and board[row][col - 1] == 'M':
            cnt += 1
        if col + 1 < cols and board[row][col + 1] == 'M':
            cnt += 1
        if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] == 'M':
            cnt += 1
        if row + 1 < rows and col + 1 < cols and board[row + 1][col + 1] == 'M':
            cnt += 1
        if row - 1 >= 0 and col + 1 < cols and board[row - 1][col + 1] == 'M':
            cnt += 1
        if col - 1 >= 0 and row + 1 < rows and board[row + 1][col - 1] == 'M':
            cnt += 1
        return cnt


    def updateBoard(self, board, click):
        row = click[0]
        col = click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        if board[row][col] == 'E':
            board[row][col] = 'B'
            cnt = self.check(board, click)
            if cnt == 0:
                rows = len(board)
                cols = len(board[0])
                if row-1 >= 0 and board[row-1][col] == 'E':
                    self.updateBoard(board, [row-1, col])
                if row + 1 < rows and board[row + 1][col] == 'E':
                    self.updateBoard(board, [row + 1, col])
                if col - 1 >= 0 and board[row][col-1] == 'E':
                    self.updateBoard(board, [row, col-1])
                if col + 1 < cols and board[row][col+1] == 'E':
                    self.updateBoard(board, [row, col+1])
                if row-1 >= 0 and col - 1 >= 0 and board[row-1][col-1] == 'E':
                    self.updateBoard(board, [row-1, col-1])
                if row + 1 < rows and col + 1 < cols and board[row + 1][col+1] == 'E':
                    self.updateBoard(board, [row + 1, col])
                if row - 1 >= 0 and col + 1 < cols and board[row-1][col+1] == 'E':
                    self.updateBoard(board, [row-1, col+1])
                if col - 1 >= 0 and row+1 < rows and board[row+1][col-1] == 'E':
                    self.updateBoard(board, [row+1, col-1])
            else:
                board[row][col] = str(cnt)
        return board

if __name__ == '__main__':
    solution = Solution()
    board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    print solution.updateBoard(board, click)