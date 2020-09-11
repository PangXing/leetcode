# coding:utf-8

# [1, 2, 4]
# [3, 5]
# [6, 7, 8]
# [1, 3, 6, 2, 5, 7, 4, 8]

def merge_list(l1):
    idx = 0
    res = list()
    flag = True
    while flag:
        flag = False
        for i in l1:
            if idx < len(i):
                res.append(i[idx])
                flag = True
        idx += 1
    return res

if __name__ == '__main__':
    l1 = [
        [1,2,4],
        [3,5],
        [6,7,8]
    ]
    print merge_list(l1)