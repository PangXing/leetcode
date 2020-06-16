# coding:utf-8

class Solution(object):
    def maximalSquare(self, matrix):
        def _get_edge_num(matrix, row, col, edge_num):
            star_col = col - edge_num
            edge_num = 0
            for i in range(col-1, star_col-1, -1):
                if int(matrix[row][i]) == 1:
                    edge_num += 1
                else:
                    break
            start_row = row-edge_num
            edge_num = 1
            for i in range(row-1, start_row - 1, -1):
                if int(matrix[i][col]) == 1:
                    edge_num += 1
                else:
                    break
            return edge_num

        dp = list()
        for row in range(len(matrix)):
            dp.append(list())
            for col in range(len(matrix[0])):
                if int(matrix[row][col]) == 1:
                    dp[row].append(1)
                else:
                    dp[row].append(0)
        max_edge = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if int(matrix[row][col]) == 1:
                    row_left = row -1
                    col_up = col -1
                    if row_left >= 0 and col_up >= 0:
                        edge_num = dp[row_left][col_up]
                        if edge_num > 0:
                            edge_num = _get_edge_num(matrix, row, col, edge_num)
                            dp[row][col] = edge_num
                        else:
                            edge_num = 1
                    else:
                        edge_num = 1
                    if edge_num > max_edge:
                        max_edge = edge_num

        return max_edge*max_edge

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 0, 1, 0, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 0, 0, 1, 0]]
    matrix = [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","1"],["0","0","0","0","0"]]
    matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
    print solution.maximalSquare(matrix)

