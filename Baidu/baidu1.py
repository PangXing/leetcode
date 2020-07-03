# coding:utf-8

list1 = [
    [1, 2, 4, 5],
    [2, 3, 6, 7],
    [8, 9, 10, 12]
]
list2 = [ [1,2,3,10] ]

list3 = [[1],
         [2],
         [3],
         [10]]
list4 = []

k = 10

def find_k(l1, k):
    if not l1:
        return (-1, -1)
    row = 0
    col = len(l1[0]) -1
    while row < len(l1) and col >= 0:
        if l1[row][col] == k:
            return (row, col)
        elif l1[row][col] > k:
            col -= 1
        else:
            row += 1
    return (-1, -1)

if __name__ == '__main__':
    print find_k(list1, k)
    print find_k(list1, 13)
    print find_k(list2, k)
    print find_k(list3, k)
    print find_k(list4, k)
