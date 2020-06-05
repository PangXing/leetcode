# coding:utf-8

class Solution(object):
    def __init__(self):
        self._print_list = list()

    def printMatrix(self, maxtrix, min_row, max_row, min_col, max_col):
        for i in range(min_col, max_col+1):
            num = maxtrix[min_row][i]
            if num == 'F':
                return
            else:
                maxtrix[min_row][i] = 'F'
            self._print_list.append(num)
        min_row += 1
        for i in range(min_row, max_row + 1):
            num = maxtrix[i][max_col]
            if num == 'F':
                return
            else:
                maxtrix[i][max_col] = 'F'
            self._print_list.append(num)
        max_col -= 1
        for i in range(max_col, min_col-1, -1):
            num = maxtrix[max_row][i]
            if num == 'F':
                return
            else:
                maxtrix[max_row][i] = 'F'
            self._print_list.append(num)
        max_row -= 1
        for i in range(max_row, min_row - 1, -1):
            num = maxtrix[i][min_col]
            if num == 'F':
                return
            else:
                maxtrix[i][min_col] = 'F'
            self._print_list.append(num)
        min_col += 1
        if min_col > max_col and min_row > max_row:
            return
        self.printMatrix(maxtrix, min_row, max_row, min_col, max_col)

    def spiralOrder(self, matrix):
        if matrix:
            min_row = 0
            max_row = len(matrix) -1
            min_col =0
            max_col = len(matrix[0]) -1
            self.printMatrix(matrix, min_row, max_row, min_col, max_col)
        return self._print_list

if __name__ == '__main__':
    solution = Solution()
    print solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
