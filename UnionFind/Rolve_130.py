# coding:utf-8

from UnionFind import UF

class Solution(object):
    def solve(self, board):
        rows = len(board)
        if rows <= 1:
            return board
        cols = len(board[0])
        if cols <= 1:
            return board
        n = rows * cols
        uf = UF(n+1)
        virual_node = n #虚拟节点 标记边O节点

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    idx = r * cols + c
                    if r == 0 or r == (rows-1) or c == 0 or c == (cols-1):
                        uf.union(idx, virual_node)
                    else:
                        if board[r-1][c] == 'O':
                            uf.union(idx, (r-1)*cols + c)
                        if board[r+1][c] == 'O':
                            uf.union(idx, (r+1) * cols + c)
                        if board[r][c-1] == 'O':
                            uf.union(idx, r * cols + c -1)
                        if board[r][c+1] == 'O':
                            uf.union(idx, r * cols + c + 1)

        for r in range(rows):
            for c in range(cols):
                idx = r * cols + c
                if uf.connected(idx, virual_node):
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
        return board

if __name__ == '__main__':
    solution = Solution()
    board = [
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X'],
             ]
    board = [["X","O","X","O","X","O"],
             ["O","X","O","X","O","X"],
             ["X","O","X","O","X","O"],
             ["O","X","O","X","O","X"]]

    board = [["O","O","O"],
             ["O","O","O"],
             ["O","O","O"]]

    board = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
             ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
             ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
             ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
             ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
             ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
             ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
             ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
             ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]

    print solution.solve(board)




