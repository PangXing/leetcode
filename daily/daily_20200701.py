# coding:utf-8

class Solution(object):
    def findLength(self, A, B):
        max_len = 0
        indexs = list()
        min_arr, max_arr = (A, B) if len(A) < len(B) else (B, A)
        for i in min_arr:
            idx = {}
            for k in range(len(max_arr)):
                if max_arr[k] == i:
                    idx[k] = 1
                    max_len = 1
            indexs.append(idx)

        for i in range(1, len(indexs)):
            if indexs[i]:
                for k in indexs[i].keys():
                    if k-1 in indexs[i-1]:
                        tmp = indexs[i-1][k-1] +1
                        if tmp > max_len:
                            max_len = tmp
                        indexs[i][k] = tmp
        return max_len

if __name__ == '__main__':
    solution = Solution()
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    print solution.findLength(A, B)






