# coding:utf-8

class UnionFind(object):
    def __init__(self, n):
        self._parents = list()
        self._sizes = list()
        self._cap = n
        for i in range(n):
            self._parents.append(i)
            self._sizes.append(1)

    def find(self, p):
        while p != self._parents[p]:
            self._parents[p] = self._parents[self._parents[p]]
            p = self._parents[p]
        return p

    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        if self._sizes[parent_q] > self._sizes[parent_p]:
            self._parents[parent_p] = parent_q
            self._sizes[parent_q] += self._sizes[parent_p]

        else:
            self._parents[parent_q] = parent_p
            self._sizes[parent_p] += self._sizes[parent_q]
        self._cap -= 1

    def connected(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        return parent_p == parent_q

class Solution(object):
    def solve(self, board):
        rows = len(board)
        cols = len(board[0])
        n = rows*cols
        if n == 0:
            return
        uf = UnionFind(n+1)
        #0为 边界连接
        for i in range(rows):
            for k in range(cols):
                idx = i*cols + k
                if board[i][k] == 'O':
                    if i == 0 or i== (rows-1) or k==0 or k == (cols-1):
                        uf.union(n, idx)
                    else:
                        if board[i-1][k] == 'O':
                            uf.union((i-1)*cols+k, idx)
                        elif board[i+1][k] == 'O':
                            uf.union((i+1)*cols+k, idx)
                        elif board[i][k-1] == 'O':
                            uf.union(i*cols+k-1, idx)
                        elif board[i][k+1] == 'O':
                            uf.union(i*cols+k+1, idx)

        for i in range(rows):
            for k in range(cols):
                idx = i*cols + k
                if uf.connected(n, idx):
                    board[i][k] = 'O'
                else:
                    board[i][k] = 'X'

if __name__ == '__main__':
    solution = Solution()
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    board = [["O","X","X","O","X"],
             ["X","O","O","X","O"],
             ["X","O","X","O","X"],
             ["O","X","O","O","O"],
             ["X","X","O","X","O"]]

    solution.solve(board)
    print board